#!/usr/bin/env python3

from abc import ABC, abstractmethod, abstractproperty
from pathlib import Path
from pathos.multiprocessing import Pool
from collections import Counter

import h5py
import numpy as np
import pandas as pd
from p_tqdm import p_map

from agora.io.signal import Signal


class Grouper(ABC):
    """
    Base grouper class
    """

    files = []

    def __init__(self, dir):
        path = Path(dir)
        assert path.exists(), "Dir does not exist"
        self.files = list(path.glob("*.h5"))
        assert len(self.files), "No valid h5 files in dir"
        self.load_signals()

    def load_signals(self):
        self.signals = {f.name[:-3]: Signal(f) for f in self.files}

    @property
    def fsignal(self):
        return list(self.signals.values())[0]

    @property
    def ntimepoints(self):
        return max([s.ntimepoints for s in self.signals.values()])

    @property
    def siglist(self):
        return self.fsignal.siglist

    @property
    def siglist_grouped(self):

        if not hasattr(self, "_siglist_grouped"):
            self._siglist_grouped = siglists = Counter(
                [x for s in self.signals.values() for x in s.siglist]
            )

        for s, n in self._siglist_grouped.items():
            print(f"{s} - {n}")

    @property
    def datasets(self):
        return self.fsignal.datasets

    @abstractproperty
    def group_names():
        pass

    def concat_signal(self, path, reduce_cols=None, axis=0, pool=None, *args, **kwargs):
        if not path.startswith("/"):
            path = "/" + path

        group_names = self.group_names

        # Check the path is in a given signal
        sitems = {k: v for k, v in self.signals.items() if path in v.siglist}
        nsignals_dif = len(self.signals) - len(sitems)
        if nsignals_dif:
            print(
                f"Grouper:Warning: {nsignals_dif} signals do not contain channel {path}"
            )

        if pool or pool is None:
            if pool is None:
                pool = 8
            with Pool(pool) as p:
                signals = p.map(
                    lambda x: concat_signal_ind(
                        path, group_names, x[0], x[1], *args, **kwargs
                    ),
                    sitems.items(),
                )
        else:
            signals = []
            for name, signal in sitems.items():
                print(name)
                signals.append(
                    concat_signal_ind(path, group_names, name, signal, **kwargs)
                )

        errors = [k for s, k in zip(signals, self.signals.keys()) if s is None]
        signals = [s for s in signals if s is not None]
        if len(errors):
            print("Warning: Positions contain errors {errors}")
            assert len(signals), f"All datasets contain errors"
        sorted = pd.concat(signals, axis=axis).sort_index()
        if reduce_cols:
            sorted = sorted.apply(np.nanmean, axis=1)
            spath = path.split("/")
            sorted.name = "_".join([spath[1], spath[-1]])

        return sorted

    @property
    def ntraps(self):
        for pos, s in self.signals.items():
            with h5py.File(s.filename, "r") as f:
                print(pos, f["/trap_info/trap_locations"].shape[0])

    def traplocs(self):
        d = {}
        for pos, s in self.signals.items():
            with h5py.File(s.filename, "r") as f:
                d[pos] = f["/trap_info/trap_locations"][()]
        return d


class MetaGrouper(Grouper):
    """Group positions using metadata's 'group' number"""

    pass


class NameGrouper(Grouper):
    """
    Group a set of positions using a subsection of the name
    """

    def __init__(self, dir, by=None):
        super().__init__(dir=dir)

        if by is None:
            by = (0, -4)
        self.by = by

    @property
    def group_names(self):
        if not hasattr(self, "_group_names"):
            self._group_names = {}
            for name in self.signals.keys():
                self._group_names[name] = name[self.by[0] : self.by[1]]

        return self._group_names

    def aggregate_multisignals(self, paths=None, **kwargs):

        aggregated = pd.concat(
            [
                self.concat_signal(path, reduce_cols=np.nanmean, **kwargs)
                for path in paths
            ],
            axis=1,
        )
        # ph = pd.Series(
        #     [
        #         self.ph_from_group(x[list(aggregated.index.names).index("group")])
        #         for x in aggregated.index
        #     ],
        #     index=aggregated.index,
        #     name="media_pH",
        # )
        # self.aggregated = pd.concat((aggregated, ph), axis=1)

        return aggregated


class phGrouper(NameGrouper):
    """
    Grouper for pH calibration experiments where all surveyed media pH values
    are within a single experiment.
    """

    def __init__(self, dir, by=(3, 7)):
        super().__init__(dir=dir, by=by)

    def get_ph(self):
        self.ph = {gn: self.ph_from_group(gn) for gn in self.group_names}

    @staticmethod
    def ph_from_group(group_name):
        if group_name.startswith("ph_"):
            group_name = group_name[3:]

        return float(group_name.replace("_", "."))

    def aggregate_multisignals(self, paths):

        aggregated = pd.concat(
            [self.concat_signal(path, reduce_cols=np.nanmean) for path in paths], axis=1
        )
        ph = pd.Series(
            [
                self.ph_from_group(x[list(aggregated.index.names).index("group")])
                for x in aggregated.index
            ],
            index=aggregated.index,
            name="media_pH",
        )
        aggregated = pd.concat((aggregated, ph), axis=1)

        return aggregated


def concat_signal_ind(path, group_names, group, signal, mode="retained", **kwargs):
    if mode == "retained":
        combined = signal.retained(path, **kwargs)
    if mode == "mothers":
        raise (NotImplementedError)
    elif mode == "raw":
        combined = signal.get_raw(path, **kwargs)
    elif mode == "families":
        combined = signal[path]
    combined["position"] = group
    combined["group"] = group_names[group]
    combined.set_index(["group", "position"], inplace=True, append=True)
    combined.index = combined.index.swaplevel(-2, 0).swaplevel(-1, 1)

    return combined
    # except:
    #     return None

#!/usr/bin/env python3

import numpy as np
import pandas as pd

from agora.abc import ParametersABC
from postprocessor.core.abc import PostProcessABC


def df_extend_nan(df, width):
    """Extend a DataFrame to the left by a number of columns and fill with NaNs

    Assumes column names are sequential integers from 0
    """
    num_rows, _ = df.shape
    nan_df = pd.DataFrame(
        np.full([num_rows, width], np.nan),
        index=df.index,
    )
    out_df = pd.concat([nan_df, df], axis=1)
    _, out_num_cols = out_df.shape
    out_df.columns = list(range(out_num_cols))
    return out_df


def df_shift(df, list_index, shift_list):
    """Shifts each row of each DataFrame by a list of shift intervals

    Assumes all DataFrames have the same indices (and therefore the same number of rows)
    """
    for index, shift in zip(list_index, shift_list):
        df.loc[index, :] = df.loc[index, :].shift(periods=shift)
    return df


class alignParameters(ParametersABC):
    """
    Parameters for the 'align' process.

    Attributes
    ----------
    slice_before_first_event: bool
        Whether to discard the parts of signals that occur before the first
        event being aligned.  For example, whether to discard flavin
        fluorescence before the first birth event, after aligning by the first
        birth event.
    events_at_least: int
        Specifies the number of events required for each cell.  For example, if
        events_at_least is 2, then it will discard time series (from the DataFrame)
        that have less than 2 events.  As a more pratical example: discarding
        flavin time series that derive from cells with less than 2 births
        identified.
    """

    _defaults = {
        "slice_before_first_event": True,
        "events_at_least": 1,
    }


class align(PostProcessABC):
    """
    Process to align a signal by corresponding events.

    For example, aligning flavin fluorescence time series by the first birth
    event of the cell each time series is derived from.

    Methods
    -------
    run(trace_df: pd.DataFrame, mask_df: pd.DataFrame)
        Align signals by events.
    """

    def __init__(self, parameters: alignParameters):
        super().__init__(parameters)

    # Not sure if having two DataFrame inputs fits the paradigm, but having the
    # mask_df be a parameter is a bit odd as it doesn't set the behaviour of the
    # process.
    def run(self, trace_df: pd.DataFrame, mask_df: pd.DataFrame):
        """Align signals by events.

        Parameters
        ----------
        trace_df : pd.DataFrame
            Signal time series, with rows indicating individual time series
            (e.g. from each cell), and columns indicating time points.
        mask_df : pd.DataFrame
            Event time series/mask, with rows indicating individual cells and
            columns indicating time points. The values of each element are
            either 0 or 1 -- 0 indicating the absence of the event, and 1
            indicating the presence of the event. Effectively, this DataFrame is
            like a mask. For example, this DataFrame can indicate when birth
            events are identified for each cell in a dataset.
        """
        # Remove cells that have less than or equal to events_at_least events,
        # i.e. if events_at_least = 1, then cells that have no birth events are
        # deleted.
        event_mask = mask_df.apply(lambda x: np.sum(x) >= self.events_at_least, axis=1)
        mask_df = mask_df.iloc[event_mask.to_list()]

        # Match trace and event signals by index, e.g. cellID
        # and discard the cells they don't have in common
        common_index = trace_df.index.intersection(mask_df.index)
        trace_aligned = trace_df.loc[common_index]
        mask_aligned = mask_df.loc[common_index]

        # Identify first event and define shift
        shift_list = []
        for index in common_index:
            event_locs = np.where(mask_df.loc[index].to_numpy() == 1)[0]
            if event_locs.any():
                shift = event_locs[0]
            else:
                shift = 0
            shift_list.append(shift)
        shift_list = np.array(shift_list)

        # Shifting

        # Remove bits of traces before first event
        if self.slice_before_first_event:
            # minus sign in front of shift_list to shift to the left
            mask_aligned = df_shift(mask_aligned, common_index.to_list(), -shift_list)
            trace_aligned = df_shift(trace_aligned, common_index.to_list(), -shift_list)
        # Do not remove bits of traces before first event
        else:
            # Add columns to left, filled with NaNs
            max_shift = np.max(shift_list)
            mask_aligned = df_extend_nan(mask_aligned, max_shift)
            trace_aligned = df_extend_nan(trace_aligned, max_shift)
            # shift each
            mask_aligned = df_shift(mask_aligned, common_index.to_list(), -shift_list)
            trace_aligned = df_shift(trace_aligned, common_index.to_list(), -shift_list)

        return trace_aligned, mask_aligned

"""Discretization of continuous columns so discrete CI tests can be applied.

The discrete G-test path needs categorical data. Common strategies:
  - equal-width binning
  - equal-frequency (quantile) binning  <- usually preferred, robust to skew
  - MDL / entropy-based (supervised)    <- best but more complex

Quantile binning is implemented; the others are left as exercises.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def quantile_bin(series: pd.Series, n_bins: int = 4) -> pd.Series:
    """Equal-frequency binning into integer codes 0..n_bins-1."""
    try:
        codes = pd.qcut(series, q=n_bins, labels=False, duplicates="drop")
    except ValueError:
        codes = pd.cut(series, bins=n_bins, labels=False)
    return codes.astype("Int64")


def discretize(df: pd.DataFrame, n_bins: int = 4,
               columns: list[str] | None = None) -> pd.DataFrame:
    """Discretize the given (or all numeric, non-integer-coded) columns."""
    out = df.copy()
    cols = columns or [c for c in df.columns
                       if pd.api.types.is_float_dtype(df[c])]
    for c in cols:
        out[c] = quantile_bin(df[c], n_bins)
    return out

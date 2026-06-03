"""Entropy estimators for discrete variables.

All quantities are in **nats** (natural log) by default; pass base=2 for bits.

Definitions
-----------
H(X)     = -Σ_x  p(x) log p(x)
H(X,Y)   = -Σ_xy p(x,y) log p(x,y)
H(X|Y)   = H(X,Y) - H(Y)

These are the building blocks of mutual information and the CI tests.
"""
from __future__ import annotations

import numpy as np


def _as_2d(*cols: np.ndarray) -> np.ndarray:
    """Stack 1-D label arrays into an (n_samples, n_cols) integer-coded matrix."""
    arrs = [np.asarray(c).reshape(-1) for c in cols]
    n = arrs[0].shape[0]
    for a in arrs:
        if a.shape[0] != n:
            raise ValueError("All variables must have the same number of samples.")
    return np.column_stack(arrs)


def _joint_counts(data: np.ndarray) -> np.ndarray:
    """Counts of each unique row (joint configuration)."""
    # Encode each unique row as a single key.
    _, inverse = np.unique(data, axis=0, return_inverse=True)
    return np.bincount(inverse)


def entropy(x: np.ndarray, base: float | None = None) -> float:
    """Shannon entropy H(X) of a single discrete variable."""
    counts = np.bincount(np.unique(np.asarray(x).reshape(-1), return_inverse=True)[1])
    p = counts / counts.sum()
    h = -np.sum(p * np.log(p + (p == 0)))  # 0 log 0 := 0
    return h / np.log(base) if base else float(h)


def joint_entropy(*cols: np.ndarray, base: float | None = None) -> float:
    """Joint entropy H(X1, ..., Xk)."""
    data = _as_2d(*cols)
    counts = _joint_counts(data)
    p = counts / counts.sum()
    h = -np.sum(p * np.log(p + (p == 0)))
    return h / np.log(base) if base else float(h)


def conditional_entropy(x: np.ndarray, *given: np.ndarray, base: float | None = None) -> float:
    """Conditional entropy H(X | given) = H(X, given) - H(given)."""
    return joint_entropy(x, *given, base=base) - joint_entropy(*given, base=base)

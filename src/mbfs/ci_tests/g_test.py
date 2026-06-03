"""G-test (likelihood-ratio test) for conditional independence on discrete data.

The G statistic is a direct rescaling of conditional mutual information:

    G = 2 * N * I(X;Y|Z)        (with I in nats)

Under H0 (X ⊥ Y | Z), G is asymptotically chi-square distributed with

    dof = Σ_z (|X_z| - 1) (|Y_z| - 1)

where |X_z|, |Y_z| are the numbers of values of X, Y that actually occur in
stratum z (this "adjusted" dof handles structural zeros better than the naive
product (|X|-1)(|Y|-1)(|Z|)). This is the canonical test used by GS and IAMB.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import chi2

from .base import CITest, CITestResult


def _contingency(x: np.ndarray, y: np.ndarray, z: list[np.ndarray]):
    """Yield per-stratum 2-D contingency tables (one per configuration of Z)."""
    if not z:
        yield _table(x, y)
        return
    zmat = np.column_stack([np.asarray(c).reshape(-1) for c in z])
    _, inv = np.unique(zmat, axis=0, return_inverse=True)
    for stratum in range(inv.max() + 1):
        mask = inv == stratum
        yield _table(x[mask], y[mask])


def _table(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    xs, xi = np.unique(x, return_inverse=True)
    ys, yi = np.unique(y, return_inverse=True)
    tab = np.zeros((len(xs), len(ys)), dtype=float)
    np.add.at(tab, (xi, yi), 1)
    return tab


def g_statistic(x: np.ndarray, y: np.ndarray, z: list[np.ndarray]) -> tuple[float, int]:
    """Compute the G statistic and adjusted degrees of freedom."""
    g = 0.0
    dof = 0
    for tab in _contingency(x, y, z):
        n = tab.sum()
        if n == 0:
            continue
        row = tab.sum(axis=1, keepdims=True)
        col = tab.sum(axis=0, keepdims=True)
        expected = row @ col / n
        nz = (tab > 0) & (expected > 0)
        g += 2.0 * np.sum(tab[nz] * np.log(tab[nz] / expected[nz]))
        # adjusted dof: only rows/cols that actually appear in this stratum
        r = int(np.count_nonzero(row))
        c = int(np.count_nonzero(col))
        dof += max(r - 1, 0) * max(c - 1, 0)
    return g, max(dof, 1)


class GTest(CITest):
    def _test(self, x, y, z) -> CITestResult:
        g, dof = g_statistic(x, y, z)
        p = float(chi2.sf(g, dof))
        return CITestResult(statistic=float(g), p_value=p, dof=dof)

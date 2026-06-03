"""Estimators for mutual information on continuous / mixed data.

The discrete plug-in estimators in entropy.py / mutual_info.py are exact given
the empirical distribution but biased for small samples. For continuous data,
use a k-NN estimator (Kraskov-Stögbauer-Grassberger, KSG).

This module is a STUB — implement after the discrete path works end-to-end.

References
----------
Kraskov, Stögbauer, Grassberger (2004), "Estimating mutual information",
Phys. Rev. E 69, 066138.  (KSG estimators 1 and 2.)
"""
from __future__ import annotations

import numpy as np


def ksg_mutual_information(x: np.ndarray, y: np.ndarray, k: int = 3) -> float:
    """KSG k-NN mutual information estimator (estimator 1).

    TODO: implement using scipy.spatial.cKDTree:
      1. Build joint space (x, y).
      2. For each point, find distance to k-th neighbor in joint (Chebyshev).
      3. Count neighbors within that distance in each marginal: n_x, n_y.
      4. I = digamma(k) + digamma(N) - <digamma(n_x+1) + digamma(n_y+1)>.
    """
    raise NotImplementedError("KSG estimator not yet implemented — see docstring.")


def miller_madow_correction(counts: np.ndarray, n: int) -> float:
    """Miller-Madow bias correction term: (#nonzero_bins - 1) / (2N).

    Add this to the plug-in discrete entropy to reduce small-sample bias.
    """
    nonzero = int(np.count_nonzero(counts))
    return (nonzero - 1) / (2 * n)

"""Permutation-based CI test using conditional mutual information.

When asymptotic chi-square assumptions are shaky (sparse strata, small N), a
permutation test gives a calibrated p-value for the null I(X;Y|Z) = 0:

  1. Compute observed CMI: t_obs = I(X;Y|Z).
  2. Repeatedly permute X *within each stratum of Z* (preserving P(X|Z) and
     P(Y|Z) but breaking any X-Y link given Z) and recompute CMI.
  3. p = (#{t_perm >= t_obs} + 1) / (n_perm + 1).

Within-stratum permutation is what makes this a valid CONDITIONAL test.
"""
from __future__ import annotations

import numpy as np

from ..info_theory.mutual_info import conditional_mutual_information
from .base import CITest, CITestResult


class MITest(CITest):
    def __init__(self, data, n_perm: int = 500, random_state: int | None = None):
        super().__init__(data)
        self.n_perm = n_perm
        self.rng = np.random.default_rng(random_state)

    def _strata(self, z: list[np.ndarray]) -> np.ndarray:
        if not z:
            return np.zeros(len(self.data), dtype=int)
        zmat = np.column_stack([np.asarray(c).reshape(-1) for c in z])
        _, inv = np.unique(zmat, axis=0, return_inverse=True)
        return inv

    def _test(self, x, y, z) -> CITestResult:
        t_obs = conditional_mutual_information(x, y, z if z else None)
        strata = self._strata(z)
        count = 0
        for _ in range(self.n_perm):
            xp = x.copy()
            for s in np.unique(strata):
                idx = np.where(strata == s)[0]
                xp[idx] = x[idx][self.rng.permutation(len(idx))]
            if conditional_mutual_information(xp, y, z if z else None) >= t_obs:
                count += 1
        p = (count + 1) / (self.n_perm + 1)
        return CITestResult(statistic=float(t_obs), p_value=float(p))

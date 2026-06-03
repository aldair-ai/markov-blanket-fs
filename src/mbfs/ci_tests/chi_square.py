"""Pearson chi-square test for conditional independence (discrete data).

Asymptotically equivalent to the G-test; uses (O-E)^2 / E instead of the
likelihood ratio. Provided so algorithms can be benchmarked across tests.

STUB: implement analogously to g_test.py, replacing the statistic with
    Σ (O - E)^2 / E   per stratum, summed, with the same adjusted dof.
"""
from __future__ import annotations

from .base import CITest, CITestResult


class ChiSquareTest(CITest):
    def _test(self, x, y, z) -> CITestResult:
        raise NotImplementedError("Mirror g_test.py with Pearson statistic.")

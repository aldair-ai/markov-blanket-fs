"""Fisher's Z test for conditional independence under a Gaussian assumption.

For multivariate-Gaussian data, X ⊥ Y | Z iff the partial correlation
rho(X,Y · Z) = 0. Fisher's z-transform gives an approximately normal statistic:

    z = sqrt(N - |Z| - 3) * 0.5 * ln((1 + r) / (1 - r))

where r is the partial correlation, computed from the inverse covariance
(precision) matrix. This is the standard CI test for continuous linear-Gaussian
networks (e.g. used in the PC algorithm).

STUB: implement after the discrete path is solid.
  1. Compute correlation matrix of [X, Y, Z].
  2. Partial correlation via the precision matrix:
         rho = -P[xy] / sqrt(P[xx] P[yy]).
  3. Apply z-transform and compare to a normal distribution (two-sided).
"""
from __future__ import annotations

from .base import CITest, CITestResult


class FisherZTest(CITest):
    def _test(self, x, y, z) -> CITestResult:
        raise NotImplementedError("Implement partial-correlation Fisher's Z test.")

"""The conditional-independence (CI) test interface.

Every MB discovery algorithm depends ONLY on this interface, never on a concrete
test. Swapping G-test for Fisher's Z (Gaussian) or an MI permutation test must
not require touching any algorithm.

A CI test answers: "Is X ⊥ Y | Z ?" given finite data, returning a test
statistic and a p-value. Algorithms compare the p-value to a significance
level alpha:

    p_value > alpha   →  fail to reject independence  →  treat as INDEPENDENT
    p_value <= alpha  →  reject independence          →  treat as DEPENDENT

Note the asymmetry of hypothesis testing: failing to reject is not proof of
independence, especially with small samples / large conditioning sets.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class CITestResult:
    statistic: float
    p_value: float
    dof: int | None = None

    def independent(self, alpha: float) -> bool:
        return self.p_value > alpha


class CITest(ABC):
    """Abstract conditional-independence test.

    Subclasses implement `_test`. The public `test` handles column lookup so
    algorithms can pass variable *names* and a DataFrame.
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data

    @abstractmethod
    def _test(self, x: np.ndarray, y: np.ndarray, z: list[np.ndarray]) -> CITestResult:
        ...

    def test(self, x: str, y: str, z: list[str] | None = None) -> CITestResult:
        z = z or []
        xv = self.data[x].to_numpy()
        yv = self.data[y].to_numpy()
        zv = [self.data[c].to_numpy() for c in z]
        return self._test(xv, yv, zv)

    def independent(self, x: str, y: str, z: list[str] | None, alpha: float) -> bool:
        return self.test(x, y, z).independent(alpha)

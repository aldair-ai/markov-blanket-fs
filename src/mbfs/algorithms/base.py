"""Base class for Markov Blanket discovery algorithms.

A discovery algorithm takes a CI test + a target name and returns the set of
variables forming the Markov Blanket of the target. Subclasses implement
`discover`.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from ..ci_tests.base import CITest


class MBDiscovery(ABC):
    def __init__(self, ci_test: CITest, alpha: float = 0.05):
        self.ci = ci_test
        self.alpha = alpha
        self.variables = [c for c in ci_test.data.columns]

    def _others(self, target: str, exclude: set[str]) -> list[str]:
        return [v for v in self.variables if v != target and v not in exclude]

    @abstractmethod
    def discover(self, target: str) -> list[str]:
        """Return the Markov Blanket of `target` as a list of variable names."""
        ...

"""Memoization for CI tests.

Discovery algorithms repeat the same CI test many times. Caching on
(x, y, frozenset(z)) — symmetric in x,y — can cut runtime dramatically.

Wrap any CITest instance:

    cached = CachedCITest(GTest(df))
    cached.test("A", "B", ["C"])   # computed
    cached.test("B", "A", ["C"])   # cache hit (symmetry)
"""
from __future__ import annotations

from .. ci_tests.base import CITest, CITestResult


class CachedCITest(CITest):
    def __init__(self, inner: CITest):
        self.inner = inner
        self.data = inner.data
        self._cache: dict = {}
        self.calls = 0
        self.hits = 0

    def _key(self, x: str, y: str, z: list[str]):
        a, b = sorted((x, y))  # symmetry: I(X;Y|Z) == I(Y;X|Z)
        return (a, b, frozenset(z))

    def test(self, x: str, y: str, z: list[str] | None = None) -> CITestResult:
        z = z or []
        self.calls += 1
        key = self._key(x, y, z)
        if key in self._cache:
            self.hits += 1
            return self._cache[key]
        result = self.inner.test(x, y, z)
        self._cache[key] = result
        return result

    def _test(self, x, y, z):  # not used; test() is overridden
        raise NotImplementedError

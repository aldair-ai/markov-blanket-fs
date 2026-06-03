from .base import CITest, CITestResult
from .g_test import GTest
from .mi_test import MITest

__all__ = ["CITest", "CITestResult", "GTest", "MITest", "get_ci_test"]


def get_ci_test(name: str, data, **kwargs) -> CITest:
    """Factory: map a string name to a concrete CI test."""
    name = name.lower()
    if name in ("g", "g_test", "gsq"):
        return GTest(data, **kwargs)
    if name in ("mi", "mi_test", "permutation"):
        return MITest(data, **kwargs)
    raise ValueError(f"Unknown CI test: {name!r}")

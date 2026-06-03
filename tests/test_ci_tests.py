import numpy as np
import pandas as pd

from mbfs.ci_tests import GTest


def _data(seed=0, n=5000):
    rng = np.random.default_rng(seed)
    a = rng.integers(0, 2, n)
    b = a.copy()                       # b depends on a
    c = rng.integers(0, 2, n)          # independent
    return pd.DataFrame({"A": a, "B": b, "C": c})


def test_gtest_detects_dependence():
    df = _data()
    res = GTest(df).test("A", "B")
    assert res.p_value < 0.01           # dependent


def test_gtest_detects_independence():
    df = _data()
    res = GTest(df).test("A", "C")
    assert res.p_value > 0.05           # independent


def test_gtest_conditional_independence():
    # B is a deterministic copy of A; given A, B ⊥ C trivially
    df = _data()
    res = GTest(df).test("B", "C", ["A"])
    assert res.p_value > 0.05

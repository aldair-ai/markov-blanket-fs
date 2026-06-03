import numpy as np

from mbfs.info_theory import (
    entropy, conditional_entropy,
    mutual_information, conditional_mutual_information,
)


def test_entropy_uniform_binary():
    x = np.array([0, 1] * 500)
    assert abs(entropy(x, base=2) - 1.0) < 1e-9  # 1 bit


def test_entropy_constant_is_zero():
    assert entropy(np.zeros(100)) == 0.0


def test_mi_independent_near_zero():
    rng = np.random.default_rng(0)
    x = rng.integers(0, 2, 5000)
    y = rng.integers(0, 2, 5000)
    assert mutual_information(x, y) < 0.01


def test_mi_identical_equals_entropy():
    rng = np.random.default_rng(0)
    x = rng.integers(0, 3, 5000)
    assert abs(mutual_information(x, x) - entropy(x)) < 1e-9


def test_cmi_explains_away():
    # Y = X, but given X the dependence of a noisy copy vanishes.
    rng = np.random.default_rng(0)
    x = rng.integers(0, 2, 5000)
    y = x.copy()
    z = x.copy()
    # I(X;Y|Z) should be ~0 since Z=X fully determines both
    assert conditional_mutual_information(x, y, z) < 0.01


def test_conditional_entropy_chain():
    rng = np.random.default_rng(0)
    x = rng.integers(0, 2, 5000)
    y = rng.integers(0, 2, 5000)
    # H(X|Y) <= H(X)
    assert conditional_entropy(x, y) <= entropy(x) + 1e-9

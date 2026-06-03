"""The most important tests: can algorithms recover a KNOWN Markov Blanket?"""
import pytest

from mbfs.algorithms import GrowShrink, IAMB
from mbfs.ci_tests import GTest
from mbfs.datasets import collider_network, chain_network


@pytest.mark.parametrize("Algo", [GrowShrink, IAMB])
def test_chain_network(Algo):
    df, true_mb = chain_network(n=8000, seed=1)
    algo = Algo(GTest(df), alpha=0.05)
    found = set(algo.discover("T"))
    assert found == true_mb


@pytest.mark.parametrize("Algo", [GrowShrink, IAMB])
def test_collider_network_recovers_spouse(Algo):
    # The hard case: T has a spouse (B, S) via the collider C.
    df, true_mb = collider_network(n=8000, seed=1)
    algo = Algo(GTest(df), alpha=0.05)
    found = set(algo.discover("T"))
    # Must include parent A and child C; the spouses come in via C.
    assert {"A", "C"} <= found
    assert "D" not in found             # never include the irrelevant variable
    assert found == true_mb

"""Synthetic Bayesian networks with KNOWN Markov Blankets, for validation.

Everything downstream is validated against these: if an algorithm cannot recover
the MB of a network you built, the bug is in the algorithm or CI test, not in
your assumptions.

`collider_network` is the key test case because it contains a SPOUSE, which
distinguishes a true MB algorithm from a mere parents/children finder.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _bernoulli(p, rng):
    return (rng.random(len(p) if hasattr(p, "__len__") else p) < p).astype(int)


def collider_network(n: int = 5000, seed: int = 0):
    """A network with a collider so that T has a spouse.

    Structure (arrows = causal direction):

        A → T → C ← S
                ↑
                B → C

      Parents(T)  = {A}
      Children(T) = {C}
      Spouses(T)  = {B, S}   (other parents of the common child C)
      => MB(T) = {A, C, B, S}

      D is an independent noise variable (NOT in the blanket).

    Returns (DataFrame, true_mb_set).
    """
    rng = np.random.default_rng(seed)

    A = _bernoulli(np.full(n, 0.5), rng)
    B = _bernoulli(np.full(n, 0.5), rng)
    S = _bernoulli(np.full(n, 0.5), rng)
    D = _bernoulli(np.full(n, 0.5), rng)  # irrelevant

    # T depends on A
    pT = np.where(A == 1, 0.8, 0.2)
    T = _bernoulli(pT, rng)

    # C (child of T) is a collider: depends on T, B, S
    logit = -1.5 + 1.6 * T + 1.6 * B + 1.6 * S
    pC = 1 / (1 + np.exp(-logit))
    C = _bernoulli(pC, rng)

    df = pd.DataFrame({"A": A, "B": B, "S": S, "T": T, "C": C, "D": D})
    true_mb = {"A", "C", "B", "S"}
    return df, true_mb


def chain_network(n: int = 5000, seed: int = 0):
    """Simple Markov chain  X1 → X2 → T → X3 → X4.

      MB(T) = {X2, X3}  (parent X2, child X3; no spouses).
    """
    rng = np.random.default_rng(seed)
    X1 = _bernoulli(np.full(n, 0.5), rng)
    X2 = _bernoulli(np.where(X1 == 1, 0.8, 0.2), rng)
    T = _bernoulli(np.where(X2 == 1, 0.8, 0.2), rng)
    X3 = _bernoulli(np.where(T == 1, 0.8, 0.2), rng)
    X4 = _bernoulli(np.where(X3 == 1, 0.8, 0.2), rng)
    df = pd.DataFrame({"X1": X1, "X2": X2, "T": T, "X3": X3, "X4": X4})
    return df, {"X2", "X3"}

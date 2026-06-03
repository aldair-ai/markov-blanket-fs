"""Mutual information and conditional mutual information for discrete variables.

I(X;Y)      = H(X) + H(Y) - H(X,Y)
            = H(X) - H(X|Y)                         (information X gives about Y)

I(X;Y|Z)    = H(X|Z) + H(Y|Z) - H(X,Y|Z)
            = H(X,Z) + H(Y,Z) - H(X,Y,Z) - H(Z)     (the MB-discovery workhorse)

CMI is the central quantity for Markov Blanket discovery:
    I(X;Y|Z) = 0  ⟺  X ⊥ Y | Z   (population level)
A high-quality estimate of I(X;Y|Z) underlies the MI-based CI test.
"""
from __future__ import annotations

import numpy as np

from .entropy import joint_entropy


def mutual_information(x: np.ndarray, y: np.ndarray, base: float | None = None) -> float:
    """Mutual information I(X;Y) >= 0."""
    hx = joint_entropy(x, base=base)
    hy = joint_entropy(y, base=base)
    hxy = joint_entropy(x, y, base=base)
    return max(0.0, hx + hy - hxy)


def conditional_mutual_information(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray | list[np.ndarray] | None = None,
    base: float | None = None,
) -> float:
    """Conditional mutual information I(X;Y|Z).

    z may be None (reduces to I(X;Y)), a single array, or a list of arrays
    (the conditioning set is their joint configuration).
    """
    if z is None or (isinstance(z, (list, tuple)) and len(z) == 0):
        return mutual_information(x, y, base=base)

    zs = list(z) if isinstance(z, (list, tuple)) else [z]
    h_xz = joint_entropy(x, *zs, base=base)
    h_yz = joint_entropy(y, *zs, base=base)
    h_xyz = joint_entropy(x, y, *zs, base=base)
    h_z = joint_entropy(*zs, base=base)
    return max(0.0, h_xz + h_yz - h_xyz - h_z)

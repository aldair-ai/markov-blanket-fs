r"""Grow-Shrink (GS) Markov Blanket discovery — Margaritis & Thrun (1999).

The original, simplest correct MB algorithm. Two phases:

GROW phase
----------
Start with empty blanket S = {}. While any variable X (not in S) is dependent
on the target T given the current S, add it:

    if  NOT (X ⊥ T | S):  S ← S ∪ {X}

This may add false positives (variables that became relevant only because S was
incomplete), so a cleanup is required.

SHRINK phase
------------
Remove any X in S that is independent of T given the REST of S:

    if  X ⊥ T | (S \ {X}):  S ← S \ {X}

Under faithfulness and a perfect CI oracle, the result equals MB(T) exactly.

Practical notes
---------------
* GS is order-dependent; a common heuristic is to consider candidates in
  decreasing order of marginal association with T (done here).
* The conditioning set in the grow phase can become large → CI tests get
  unreliable. IAMB mitigates this by always adding the *most* associated
  candidate first.
"""
from __future__ import annotations

from .base import MBDiscovery


class GrowShrink(MBDiscovery):
    def discover(self, target: str) -> list[str]:
        S: list[str] = []

        # ---- GROW ----
        changed = True
        while changed:
            changed = False
            # order candidates by association with T given current S
            candidates = self._others(target, exclude=set(S))
            scored = sorted(
                candidates,
                key=lambda x: self.ci.test(x, target, S).statistic,
                reverse=True,
            )
            for x in scored:
                if not self.ci.independent(x, target, S, self.alpha):
                    S.append(x)
                    changed = True
                    break  # recompute ordering with the enlarged S

        # ---- SHRINK ----
        changed = True
        while changed:
            changed = False
            for x in list(S):
                rest = [v for v in S if v != x]
                if self.ci.independent(x, target, rest, self.alpha):
                    S.remove(x)
                    changed = True
                    break

        return S

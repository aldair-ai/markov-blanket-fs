r"""IAMB — Incremental Association Markov Blanket (Tsamardinos & Aliferis, 2003).

Improves on Grow-Shrink by being smarter about WHICH variable to add: at each
grow step it adds the candidate with the *maximum* association with T given the
current blanket. This keeps the blanket small during growth, so conditioning
sets stay small and CI tests stay reliable.

GROW (forward)
--------------
Repeat: among all X not in CMB, pick the one maximizing association
f(X) = statistic of test(X, T | CMB). If that X is still dependent on T given
CMB (p <= alpha), add it. Stop when no candidate is dependent.

SHRINK (backward)
-----------------
Same as GS: drop any X with  X ⊥ T | (CMB \ {X}).

Association measure: here we use the CI test statistic itself (G ∝ CMI), which
is the conventional choice.
"""
from __future__ import annotations

from .base import MBDiscovery


class IAMB(MBDiscovery):
    def discover(self, target: str) -> list[str]:
        cmb: list[str] = []

        # ---- GROW: add max-association dependent variable ----
        while True:
            candidates = self._others(target, exclude=set(cmb))
            if not candidates:
                break
            best, best_stat, best_dep = None, -1.0, False
            for x in candidates:
                res = self.ci.test(x, target, cmb)
                if res.statistic > best_stat:
                    best, best_stat = x, res.statistic
                    best_dep = not res.independent(self.alpha)
            if best is not None and best_dep:
                cmb.append(best)
            else:
                break

        # ---- SHRINK ----
        changed = True
        while changed:
            changed = False
            for x in list(cmb):
                rest = [v for v in cmb if v != x]
                if self.ci.independent(x, target, rest, self.alpha):
                    cmb.remove(x)
                    changed = True
                    break

        return cmb

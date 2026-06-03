"""MMMB — Max-Min Markov Blanket (Tsamardinos, Aliferis, Statnikov, 2003).

Built on MMPC (Max-Min Parents and Children):

  MMPC selects candidates by the "max-min" heuristic: repeatedly add the
  variable whose MINIMUM association with T over all subsets of the current
  candidate set is MAXIMUM. This admits a variable only if it stays associated
  with T across every conditioning subset tried — strong false-positive control.

MMMB then:
  1. Compute PC(T) via MMPC.
  2. Compute PC(X) for each X in PC(T).
  3. Recover spouses: candidate spouses come from the PC sets of T's children;
     keep Y if it is dependent on T given some set containing the common child.
  4. MB(T) = PC(T) ∪ spouses.

STUB: implement MMPC (with the max-min subset search), then the spouse step.
Compare against HITON-MB on the same benchmark — they should largely agree.
"""
from __future__ import annotations

from .base import MBDiscovery


class MMMB(MBDiscovery):
    def discover(self, target: str) -> list[str]:
        raise NotImplementedError("Implement MMPC (max-min) then spouse recovery.")

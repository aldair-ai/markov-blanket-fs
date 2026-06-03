"""HITON-MB (Aliferis, Tsamardinos, Statnikov, 2003).

A topology-aware ("local discovery") family. Unlike IAMB which conditions on the
whole growing blanket, HITON finds structure first:

  1. HITON-PC: find the parents-and-children set PC(T) of the target using the
     MaxMin / interleaved heuristic with conditioning over SUBSETS of the
     current PC (not the whole set) — more sample-efficient.
  2. For each X in PC(T), find PC(X). Any Y in some PC(X) that is dependent on T
     given {X} ∪ (some subset) but was not in PC(T) is a SPOUSE → add it.
  3. MB(T) = PC(T) ∪ spouses(T).

The spouse-discovery step is what distinguishes MB from PC: spouses are
co-parents of T's children (the colliders).

STUB: implement HITON-PC first (subset-based CI conditioning), then the spouse
recovery step. Validate that on a known network it recovers parents + children +
spouses exactly.
"""
from __future__ import annotations

from .base import MBDiscovery


class HITONMB(MBDiscovery):
    def discover(self, target: str) -> list[str]:
        raise NotImplementedError("Implement HITON-PC then spouse recovery.")

"""Inter-IAMB — interleaved IAMB (Tsamardinos et al.).

Interleaves the shrink phase INTO the grow phase: after every single addition,
immediately run a shrink pass. This keeps the candidate Markov blanket as small
as possible at every step, further improving CI-test reliability and reducing
false positives versus plain IAMB.

STUB: implement by taking IAMB.discover and, right after `cmb.append(best)`,
running the shrink loop before continuing the grow loop.
"""
from __future__ import annotations

from .iamb import IAMB


class InterIAMB(IAMB):
    def discover(self, target: str) -> list[str]:
        raise NotImplementedError(
            "Interleave the shrink pass after each grow addition (see docstring)."
        )

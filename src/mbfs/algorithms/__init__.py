from .base import MBDiscovery
from .grow_shrink import GrowShrink
from .iamb import IAMB
from .inter_iamb import InterIAMB
from .hiton_mb import HITONMB
from .mmmb import MMMB

ALGORITHMS = {
    "grow_shrink": GrowShrink,
    "gs": GrowShrink,
    "iamb": IAMB,
    "inter_iamb": InterIAMB,
    "hiton_mb": HITONMB,
    "mmmb": MMMB,
}

__all__ = ["MBDiscovery", "GrowShrink", "IAMB", "InterIAMB",
           "HITONMB", "MMMB", "ALGORITHMS"]

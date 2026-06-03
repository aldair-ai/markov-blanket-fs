"""Compare MB discovery algorithms against ground truth on synthetic networks."""
from mbfs.algorithms import GrowShrink, IAMB
from mbfs.ci_tests import GTest
from mbfs.utils import CachedCITest
from mbfs.datasets import collider_network, chain_network


def evaluate(found: set, true: set) -> dict:
    tp = len(found & true)
    fp = len(found - true)
    fn = len(true - found)
    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}


def main():
    for name, gen in [("chain", chain_network), ("collider", collider_network)]:
        df, true_mb = gen(n=8000, seed=1)
        print(f"\n=== {name} network — true MB(T) = {sorted(true_mb)} ===")
        for Algo in (GrowShrink, IAMB):
            ci = CachedCITest(GTest(df))
            found = set(Algo(ci, alpha=0.05).discover("T"))
            m = evaluate(found, true_mb)
            print(f"{Algo.__name__:>12}: {sorted(found)}  "
                  f"P={m['precision']:.2f} R={m['recall']:.2f} F1={m['f1']:.2f} "
                  f"(CI calls={ci.calls})")


if __name__ == "__main__":
    main()

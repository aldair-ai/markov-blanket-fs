"""Quickstart: discover the Markov Blanket of a target on a synthetic network."""
from mbfs.selector import MarkovBlanketSelector
from mbfs.datasets import collider_network


def main():
    df, true_mb = collider_network(n=8000, seed=1)
    print("Variables:", list(df.columns))
    print("True MB(T):", sorted(true_mb))

    for algo in ("grow_shrink", "iamb"):
        sel = MarkovBlanketSelector(target="T", algorithm=algo, alpha=0.05)
        sel.fit(df)
        print(f"{algo:>12}  ->  {sorted(sel.markov_blanket_)}")
        cache = sel.ci_
        print(f"{'':>12}      CI calls={cache.calls}, cache hits={cache.hits}")


if __name__ == "__main__":
    main()

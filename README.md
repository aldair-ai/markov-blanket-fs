# markov-blanket-fs

A **learn-by-building** library for feature selection based on the **Markov Blanket (MB)**.

This repo is two things at once:

1. **A learning path** — `docs/` and `notebooks/` walk you from probability/information-theory
   foundations up to full Markov Blanket discovery algorithms, so you understand *100% of the math*
   before relying on the code.
2. **A usable library** — `src/mbfs/` is an sklearn-compatible feature selector built on a clean,
   testable CI-test layer.

---

## Why the Markov Blanket?

For a target variable `T`, its Markov Blanket `MB(T)` is the **minimal** set of variables that makes
`T` conditionally independent of *everything else*:

```
T ⊥ (V \ ({T} ∪ MB(T)))  |  MB(T)
```

Under the *faithfulness* assumption, `MB(T)` is **the theoretically optimal feature set** for predicting
`T`: no other feature adds information once you condition on the blanket. That is what makes MB-based
selection principled rather than heuristic.

In a Bayesian network, `MB(T) = parents(T) ∪ children(T) ∪ spouses(T)` (co-parents of T's children).

---

## Learning Roadmap

Work through `docs/` in order. Each has a companion notebook.

| Phase | Topic | Doc | Notebook |
|-------|-------|-----|----------|
| 0 | Information theory (entropy, MI, CMI) | `docs/01_information_theory.md` | `01_entropy_and_mi.ipynb` |
| 1 | Conditional independence & tests | `docs/02_conditional_independence.md` | `02_conditional_independence_demo.ipynb` |
| 2 | Graphical models & d-separation | `docs/03_graphical_models.md` | — |
| 3 | Markov Blanket theory | `docs/04_markov_blanket_theory.md` | `03_markov_blanket_intuition.ipynb` |
| 4 | Discovery algorithms | `docs/05_discovery_algorithms.md` | `04_grow_shrink_from_scratch.ipynb` |
| 5 | CI tests in depth | `docs/06_ci_tests.md` | `05_benchmark_on_known_network.ipynb` |

---

## Quickstart

```bash
pip install -e .
python examples/quickstart.py
```

```python
from mbfs.selector import MarkovBlanketSelector

selector = MarkovBlanketSelector(target="T", algorithm="grow_shrink", alpha=0.05)
selector.fit(df)              # df: pandas DataFrame of discrete variables
print(selector.markov_blanket_)   # discovered MB of T
X_reduced = selector.transform(df)
```

---

## Build Order (for contributors)

1. `info_theory/` — entropy + MI estimators (everything depends on these)
2. `ci_tests/` — the `CITest` interface + G-test
3. `datasets/` — synthetic BN generator with *known* MB for validation
4. `algorithms/grow_shrink.py` — first full algorithm
5. IAMB → Inter-IAMB → HITON-MB → MMMB
6. `selector.py` — sklearn-compatible wrapper
7. Benchmarks + docs

## License

MIT — see `LICENSE`.

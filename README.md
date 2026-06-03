# Markov Blanket — Study Guide

A **study-only** repository for understanding the math and concepts behind
**Markov Blanket feature selection**, end to end. It contains no library — the
reusable, packaged implementation lives in a **separate repository**. The purpose
here is to understand the theory and calculus *100%* before (or alongside) using
that library.

Everything is self-contained: the notebooks build each concept from scratch with
only `numpy`, `pandas`, and `scipy`. Nothing to install but those.

---

## What's inside

```
docs/         conceptual explanations, one per phase (the "textbook")
notebooks/    self-contained runnable notebooks (the "lab")
exercises/    practice problems per phase
  solutions/  worked solutions
```

## The learning path

Work each row top to bottom: read the doc, run the notebook, do the exercises.

| Phase | Topic | Doc | Notebook | Exercises |
|-------|-------|-----|----------|-----------|
| 0 | Information theory (entropy, MI, **CMI**) | `docs/01_information_theory.md` | `notebooks/01_entropy_and_mi.ipynb` | `exercises/01_information_theory.md` |
| 1 | Conditional independence & testing | `docs/02_conditional_independence.md` | `notebooks/02_conditional_independence_demo.ipynb` | `exercises/02_conditional_independence.md` |
| 2 | Graphical models & d-separation | `docs/03_graphical_models.md` | `notebooks/03_markov_blanket_intuition.ipynb` | `exercises/03_graphical_models.md` |
| 3 | Markov Blanket theory | `docs/04_markov_blanket_theory.md` | `notebooks/03_markov_blanket_intuition.ipynb` | `exercises/04_markov_blanket_theory.md` |
| 4 | Discovery algorithms (GS, IAMB, …) | `docs/05_discovery_algorithms.md` | `notebooks/04_grow_shrink_from_scratch.ipynb` | `exercises/05_discovery_algorithms.md` |
| 5 | CI tests in depth | `docs/06_ci_tests.md` | `notebooks/05_benchmark_on_known_network.ipynb` | `exercises/06_ci_tests.md` |

Start with `docs/00_roadmap.md` for the full map.

## The one idea everything rests on

For a target `T`, its **Markov Blanket** is the minimal set that makes `T`
independent of everything else:

```
T ⊥ (V \ ({T} ∪ MB(T)))  |  MB(T)
```

In a faithful Bayesian network it equals
`parents(T) ∪ children(T) ∪ spouses(T)`. The **spouse** term — co-parents of
`T`'s children, which enter through colliders — is the subtle part, and the
notebooks build a network with a known spouse so you can verify it yourself with
conditional-independence tests.

## Quickstart

```bash
pip install -r requirements.txt
jupyter lab          # open notebooks/ in order, or read docs/ first
```

Every notebook is pre-executed (outputs included) so you can read it like a
worked example, then re-run cells to experiment.

## After this

Once these concepts are solid, move to the separate **library** repository, where
the same algorithms are packaged as a tested, sklearn-compatible feature
selector. The exercises in phases 4–5 (implementing Inter-IAMB, the HITON spouse
step, a permutation test, Fisher's Z) are good preparation for reading that code.

## License

MIT — see `LICENSE`.

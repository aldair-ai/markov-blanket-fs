# 00 — Roadmap

A guided path to **understanding** the math and concepts behind Markov Blanket
feature selection. This repository is *study-only*: every idea is explained in a
doc and made concrete in a **self-contained notebook** (all math written inline,
nothing to install beyond numpy/pandas/scipy). The actual reusable library lives
in a separate repository.

Read the docs in order; each maps to a notebook and a set of exercises.

## Phase 0 — Information Theory (`01_information_theory.md`)
Entropy, joint/conditional entropy, mutual information, **conditional mutual
information (CMI)**. CMI is the single quantity all MB discovery rests on:
`I(X;Y|Z) = 0 ⟺ X ⊥ Y | Z`.
→ Notebook: `notebooks/01_entropy_and_mi.ipynb`
→ Exercises: `exercises/01_information_theory.md`

## Phase 1 — Conditional Independence & Tests (`02_conditional_independence.md`)
What CI means, how we test it from finite data (G-test), and the asymmetry of
hypothesis testing.
→ Notebook: `notebooks/02_conditional_independence_demo.ipynb`
→ Exercises: `exercises/02_conditional_independence.md`

## Phase 2 — Graphical Models (`03_graphical_models.md`)
Bayesian networks, factorization, d-separation, faithfulness. Why the blanket
has the parents/children/spouses form.
→ Notebook: covered within `notebooks/03_markov_blanket_intuition.ipynb`
→ Exercises: `exercises/03_graphical_models.md`

## Phase 3 — Markov Blanket Theory (`04_markov_blanket_theory.md`)
Formal definition, the optimality theorem, uniqueness under faithfulness, and
the parents ∪ children ∪ spouses characterization.
→ Notebook: `notebooks/03_markov_blanket_intuition.ipynb`
→ Exercises: `exercises/04_markov_blanket_theory.md`

## Phase 4 — Discovery Algorithms (`05_discovery_algorithms.md`)
Grow-Shrink → IAMB → Inter-IAMB → HITON-MB → MMMB. What each fixes about the
previous one.
→ Notebook: `notebooks/04_grow_shrink_from_scratch.ipynb`
→ Exercises: `exercises/05_discovery_algorithms.md`

## Phase 5 — CI Tests in Depth (`06_ci_tests.md`)
Degrees of freedom, sparsity, sample-size limits, multiple testing, and how the
choice of α trades false positives against false negatives.
→ Notebook: `notebooks/05_benchmark_on_known_network.ipynb`
→ Exercises: `exercises/06_ci_tests.md`

## How to use this repo

```bash
pip install -r requirements.txt      # numpy, pandas, scipy, jupyter
jupyter lab                          # then open notebooks/ in order
```

Work the doc, run the notebook cell by cell, then do the exercises (solutions in
`exercises/solutions/`). Each notebook builds a synthetic Bayesian network with a
**known** Markov Blanket — including a spouse via a collider — so you can check
every claim against ground truth yourself.

Once these concepts feel solid, move to the separate library repository, where
the same ideas are packaged as a tested, sklearn-compatible tool.

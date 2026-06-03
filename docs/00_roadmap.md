# 00 — Roadmap

A guided path from probability foundations to a working Markov Blanket feature
selector. Read the docs in order; each maps to code you can run.

## Phase 0 — Information Theory (`01_information_theory.md`)
Entropy, joint/conditional entropy, mutual information, **conditional mutual
information (CMI)**. CMI is the single quantity all MB discovery rests on:
`I(X;Y|Z) = 0 ⟺ X ⊥ Y | Z`.
→ Code: `mbfs/info_theory/`

## Phase 1 — Conditional Independence & Tests (`02_conditional_independence.md`)
What CI means, how we test it from finite data (G-test, χ², Fisher's Z,
permutation), and the asymmetry of hypothesis testing.
→ Code: `mbfs/ci_tests/`

## Phase 2 — Graphical Models (`03_graphical_models.md`)
Bayesian networks, factorization, d-separation, faithfulness. Why the blanket
has the parents/children/spouses form.

## Phase 3 — Markov Blanket Theory (`04_markov_blanket_theory.md`)
Formal definition, the optimality theorem, uniqueness under faithfulness, and
the parents ∪ children ∪ spouses characterization.

## Phase 4 — Discovery Algorithms (`05_discovery_algorithms.md`)
Grow-Shrink → IAMB → Inter-IAMB → HITON-MB → MMMB. What each fixes about the
previous one.
→ Code: `mbfs/algorithms/`

## Phase 5 — CI Tests in Depth (`06_ci_tests.md`)
Degrees of freedom, sparsity, sample-size limits, multiple testing, and how the
choice of α trades false positives against false negatives.

## Validate everything
Use `mbfs/datasets/synthetic.py` — networks with a KNOWN Markov Blanket
(including a spouse via a collider). If your algorithm can't recover these, fix
it before moving on.

```bash
pip install -e ".[dev]"
pytest -q
python examples/compare_algorithms.py
```

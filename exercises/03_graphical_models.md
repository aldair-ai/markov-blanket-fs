# Exercises — Phase 2: Graphical Models & d-separation

Prerequisite: `docs/03_graphical_models.md`,
`notebooks/03_markov_blanket_intuition.ipynb`.
Solutions in `solutions/03_graphical_models.md`.

## E3.1 — d-separation by hand
For the network `A → T → C ← S`, `B → C`, list every variable and state whether
it is d-separated from `T` by the empty set, and by `{C}`. Check your answers
against CI tests in the notebook.

## E3.2 — The three path types
Build three minimal networks — a chain `X→M→Y`, a fork `X←M→Y`, and a collider
`X→M←Y`. For each, tabulate `I(X;Y)` and `I(X;Y|M)`. Summarize in one sentence
how conditioning on `M` behaves in each case.

## E3.3 — Descendants of a collider
Extend the collider `X→M←Y` with a child `M→W`. Show that conditioning on the
*descendant* `W` (not `M` itself) also opens the X–Y path, just more weakly.
Why does this matter for choosing a Markov Blanket?

## E3.4 — Factorization and parameter count
Write the factorization `P(A,B,S,T,C,D) = ∏ P(·|parents)` for the notebook
network. How many free parameters does it have, versus the full joint over six
binary variables? This is the practical payoff of the graph structure.

## E3.5 — A faithfulness violation
Construct a distribution where `X` and `Y` are *marginally* independent despite a
direct edge `X → Y` (hint: make the effect cancel across a third variable). Show
a CI test wrongly reports independence. Explain why faithfulness is the
assumption that rules this out — and why CI-based discovery can fail without it.

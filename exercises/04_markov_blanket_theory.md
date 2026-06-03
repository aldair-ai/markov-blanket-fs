# Exercises — Phase 3: Markov Blanket Theory

Prerequisite: `docs/04_markov_blanket_theory.md`,
`notebooks/03_markov_blanket_intuition.ipynb`.
Solutions in `solutions/04_markov_blanket_theory.md`.

## E4.1 — Identify the blanket
For the notebook network, write out `parents(T)`, `children(T)`, and
`spouses(T)` separately, then assemble `MB(T)`. Confirm each membership with the
appropriate CI test.

## E4.2 — The defining property
Verify the blanket property directly: for every variable `X` not in
`{T} ∪ MB(T)`, show `I(T; X | MB(T)) ≈ 0`. (In this network the only such `X` is
`D`.) Add a second irrelevant variable `E` and confirm it too is screened off.

## E4.3 — Minimality
Show that the blanket is *minimal*: remove each member in turn and demonstrate
that `T` becomes dependent on something outside the reduced set. Which member,
when removed, reopens a dependence with a spouse?

## E4.4 — Optimality for prediction
Train a simple classifier (e.g. logistic regression) to predict `T` from
(a) the full feature set and (b) `MB(T)` only. Compare accuracy. Then add pure
noise features to the full set and show the blanket-only model is at least as
good while using fewer features.

## E4.5 — Non-uniqueness without faithfulness
Using your faithfulness-violation construction from E3.5, exhibit a case where
two different minimal sets both satisfy the blanket property. Why does
faithfulness restore uniqueness?

## E4.6 — Blanket of a different target
Re-derive the Markov Blanket for target `C` (the collider) instead of `T`. How
does its blanket differ in composition (parents/children/spouses) from `T`'s?

# Exercises — Phase 0: Information Theory

Prerequisite: `docs/01_information_theory.md`, `notebooks/01_entropy_and_mi.ipynb`.
Solutions in `solutions/01_information_theory.md`.

## E1.1 — Entropy by hand
A four-sided die is loaded with probabilities `[0.5, 0.25, 0.125, 0.125]`.
Compute `H` in bits by hand, then verify with the `entropy` function from the
notebook. Why is it less than the 2 bits of a fair d4?

## E1.2 — The chain rule of entropy
Prove (and then verify numerically) that
`H(X, Y) = H(X) + H(Y | X)`. Generate dependent `X, Y` and show both sides match.

## E1.3 — MI is symmetric, conditioning is not
Show numerically that `I(X;Y) == I(Y;X)`, but that `I(X;Y|Z)` can be larger OR
smaller than `I(X;Y)`. Construct one example of each:
(a) conditioning *destroys* information (a chain), and
(b) conditioning *creates* information (a collider).

## E1.4 — Data-processing inequality
For a chain `X → Y → Z`, the data-processing inequality says
`I(X;Z) ≤ I(X;Y)`. Build such a chain and verify it. What does it imply about
trying to predict `X` from `Z` instead of `Y`?

## E1.5 — Miller–Madow bias correction
The plug-in entropy is biased low; the Miller–Madow correction adds
`(m̂ − 1) / (2N)`, where `m̂` is the number of observed outcomes. Implement it,
then show on small samples of an independent pair that the corrected MI is closer
to the true value of 0 than the raw plug-in estimate. (This is the estimator the
library's `estimators.py` would provide.)

## E1.6 — Bits vs nats
Re-express `I(A;B)` from notebook section 3 in both bits and nats and confirm the
ratio is exactly `ln 2`. When would you prefer each unit?

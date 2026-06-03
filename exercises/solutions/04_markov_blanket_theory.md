# Solutions — Phase 3: Markov Blanket Theory

## S4.1 — Identify the blanket
`parents(T) = {A}`, `children(T) = {C}`, `spouses(T) = {B, S}` (the other parents
of child `C`). So `MB(T) = {A, C, B, S}`. Each is confirmed in notebook 03: `A;T`
and `C;T` dependent directly; `B;T` and `S;T` dependent only given `C`.

## S4.2 — The defining property
For the only outside variable `D`: `I(T;D | {A,C,B,S}) ≈ 0` (notebook shows
p≈0.96). Adding another irrelevant `E` (independent random bit) gives the same
result — the blanket screens `T` from all non-members.

## S4.3 — Minimality
Removing `A`: `T` becomes dependent on `A` (a parent) again — recovers a direct
dependence. Removing `C`: this is the key one — dropping the child *closes* the
collider, and the spouses `B, S` are no longer reachable through it, but `T`
becomes dependent on `C` itself. Removing `B` (or `S`): `T` becomes dependent on
that spouse given the remaining `C`. Each removal reopens some dependence ⇒ the
set is minimal.

## S4.4 — Optimality for prediction
Logistic regression on the full feature set `{A,B,S,C,D}` and on the blanket
`{A,B,S,C}` give equal 5-fold accuracy (≈0.797 both). Dropping `D` costs nothing.
Adding noise features to the full set only hurts it, while the blanket model is
unchanged — the blanket is sufficient and non-redundant.

## S4.5 — Non-uniqueness without faithfulness
With the XOR cancellation from S3.5, a variable can be both includable and
excludable without changing the independence pattern, so two distinct minimal
sets satisfy the blanket property. Faithfulness forbids the cancellation, making
the d-separation pattern — and hence the Markov boundary — unique.

## S4.6 — Blanket of C
For target `C`: `parents(C) = {T, B, S}`, `children(C) = {}`, `spouses(C) = {}`
(no children ⇒ no spouses). Also include nothing further. So `MB(C) = {T, B, S}`.
Note it is all-parents and no spouses — structurally different from `T`'s blanket,
which is driven by the collider at `C`.

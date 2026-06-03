# Exercises — Phase 1: Conditional Independence & Testing

Prerequisite: `docs/02_conditional_independence.md`,
`notebooks/02_conditional_independence_demo.ipynb`.
Solutions in `solutions/02_conditional_independence.md`.

## E2.1 — Type I error rate
Under H0 (true independence), a calibrated test should reject about α of the
time. Generate 1000 independent pairs, run your `g_test` on each at α=0.05, and
report the empirical rejection rate. Is it close to 5%?

## E2.2 — Power curve
Fix a weak dependence (e.g. `P(B=A) = 0.55`). Plot (or tabulate) the rejection
rate vs sample size N over `[100, 300, 1000, 3000, 10000]`. At what N does the
test reliably (>90%) detect the dependence?

## E2.3 — Adjusted vs naive degrees of freedom
Modify `g_test` to also return the *naive* dof `(|X|−1)(|Y|−1)·(#strata)` and
compare p-values against the adjusted dof on a network with structural zeros
(some Z-strata where a value of X never occurs). Which is better calibrated?

## E2.4 — Implement Pearson's χ² test
Write `chi2_test(x, y, z)` using `Σ (O−E)²/E` per stratum with the same adjusted
dof. Confirm it agrees with the G-test on the notebook's chain network (both
should flip `A;C` to independent given `B`).

## E2.5 — The mediator vs the confounder
Build two networks that produce the *same* marginal dependence between `X` and
`Y` but for different reasons: (a) a mediator `X → M → Y`, (b) a confounder
`X ← C → Y`. Show that conditioning on the middle variable removes the
dependence in both cases. Why can't a CI test alone tell the two structures
apart?

## E2.6 — When asymptotics fail
Shrink the sample to N=80 and add 4 conditioning variables. Show that the χ²
p-value becomes unreliable (cells with expected count < 5). Sketch how a
within-stratum permutation test would fix this (see exercise E6.3).

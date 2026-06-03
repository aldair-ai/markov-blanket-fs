# Exercises — Phase 5: CI Tests in Depth

Prerequisite: `docs/06_ci_tests.md`,
`notebooks/05_benchmark_on_known_network.ipynb`.
Solutions in `solutions/06_ci_tests.md`.

## E6.1 — G equals 2N·CMI
Show numerically that the G statistic equals `2 · N · Î(X;Y|Z)` (with CMI in
nats). Compute both sides independently and confirm they match to floating-point
precision.

## E6.2 — Expected-count diagnostic
Add a check to `g_test` that warns when any cell's expected count falls below 5.
Run it across a sweep of conditioning-set sizes and report the |Z| at which the
warning first fires for fixed N.

## E6.3 — Implement a permutation CI test
Write `perm_test(x, y, z, n_perm=500)` that permutes `x` *within each stratum of
z* and compares observed CMI to the shuffled distribution. Show it agrees with
the G-test on large samples but stays calibrated where χ² breaks (small N, large
|Z| from E2.6).

## E6.4 — Sketch Fisher's Z for Gaussian data
For multivariate-Gaussian data, `X ⊥ Y | Z` iff the partial correlation is 0.
Generate linear-Gaussian data for a chain, compute the partial correlation via
the precision matrix, apply Fisher's z-transform, and test independence. Confirm
the mediator screens off as expected.

## E6.5 — Discretization trade-off
Take a continuous version of the network (Gaussian noise) and discretize with
2, 4, 8, and 16 quantile bins. Plot discovery F1 vs number of bins. Explain the
U-shape: too few bins lose signal, too many create sparse strata.

## E6.6 — Multiple-testing effect
A full discovery run performs many CI tests. Estimate how the family-wise false
positive probability grows with the number of tests at fixed α, and discuss
whether the shrink phase or a correction (e.g. Bonferroni) is the better remedy
in practice.

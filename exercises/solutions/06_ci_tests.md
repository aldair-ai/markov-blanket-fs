# Solutions — Phase 5: CI Tests in Depth

## S6.1 — G equals 2N·CMI
Verified to floating-point precision: for N=6000 we measured `G = 2233.0318` and
`2N·Î(X;Y|Z) = 2233.0318` (CMI in nats). This identity is *why* the G-test is the
natural CI test in an information-theoretic framework — the statistic literally
*is* rescaled conditional mutual information.

## S6.2 — Expected-count diagnostic
Add `if (e[nz] < 5).any(): warn(...)`. As |Z| grows at fixed N the warning fires
once strata thin out — typically around the point where `#cells ≈ N/5`. This is a
practical stop signal: beyond it, trust the test less or switch to permutation.

## S6.3 — Permutation CI test
```python
def perm_test(x, y, z=None, n_perm=500, seed=0):
    rng = np.random.default_rng(seed)
    z = z or []
    strata = (np.zeros(len(x), int) if not z else
              np.unique(np.column_stack([np.asarray(c) for c in z]),
                        axis=0, return_inverse=True)[1])
    t_obs = cmi(x, y, z if z else None)
    count = 0
    for _ in range(n_perm):
        xp = np.asarray(x).copy()
        for s in np.unique(strata):
            idx = np.where(strata == s)[0]
            xp[idx] = xp[idx][rng.permutation(len(idx))]
        if cmi(xp, y, z if z else None) >= t_obs:
            count += 1
    return (count + 1) / (n_perm + 1)
```
Within-stratum shuffling preserves `P(X|Z)` and `P(Y|Z)` while breaking any X–Y
link given Z, so it samples the conditional null directly. It matches the G-test
on large N and stays calibrated where χ² fails.

## S6.4 — Fisher's Z (Gaussian)
Compute the correlation matrix of `[X,Y,Z...]`, invert to the precision matrix
`P`, get partial correlation `r = -P[xy]/sqrt(P[xx]P[yy])`, then
`z = sqrt(N-|Z|-3)·atanh(r)` is ~N(0,1) under the null. For a linear-Gaussian
chain `X→M→Y`, the partial correlation `r(X,Y·M) ≈ 0` → independence confirmed.

## S6.5 — Discretization trade-off
F1 vs bins is U-shaped: 2 bins lose too much signal (low recall); 16 bins create
sparse strata so CI tests destabilize (precision/recall both drop). A middle
value (≈4) usually maximizes F1. Lesson: discretization granularity is a real
hyperparameter, traded off against sample size.

## S6.6 — Multiple-testing effect
With `m` independent tests at level α, the chance of at least one false positive
is `1-(1-α)^m`, rising fast with `m`. In MB discovery the **shrink phase** is the
primary safeguard (it re-tests and removes spurious additions given the fuller
conditioning set), and is usually preferred to a blanket Bonferroni correction,
which can over-shrink and hurt recall. Some implementations combine a mild
correction with shrink.

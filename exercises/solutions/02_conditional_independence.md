# Solutions — Phase 1: Conditional Independence & Testing

## S2.1 — Type I error rate
Running 1000 independent pairs (N=500) at α=0.05 gives an empirical rejection
rate ≈ 0.05–0.06 (we observed 0.058). A well-calibrated test rejects roughly α of
the time under the null. Small deviations are sampling noise; large ones signal a
mis-specified dof.

## S2.2 — Power curve
With `P(B=A)=0.55`, rejection rate rises with N. Typical pattern: ~0.1 at N=100,
climbing past 0.9 only around N≈3000–10000 for so weak an effect. Lesson: weak
dependencies need large samples; otherwise the test produces false negatives.

## S2.3 — Adjusted vs naive dof
The naive dof `(|X|−1)(|Y|−1)·#strata` over-counts when some strata never see a
particular X or Y value (structural zeros), inflating dof and making the test too
conservative (p-values too large, missed dependencies). The adjusted dof counts
only occurring rows/cols per stratum and is better calibrated.

## S2.4 — Pearson χ²
```python
def chi2_test(x, y, z=None):
    z = z or []
    stat, dof = 0.0, 0
    for tab in _strata_tables(np.asarray(x), np.asarray(y), z):
        n = tab.sum()
        if n == 0: continue
        row = tab.sum(1, keepdims=True); col = tab.sum(0, keepdims=True)
        e = row @ col / n; nz = e > 0
        stat += np.sum((tab[nz] - e[nz])**2 / e[nz])
        dof += max(int(np.count_nonzero(row))-1,0)*max(int(np.count_nonzero(col))-1,0)
    return float(stat), max(dof,1), float(chi2.sf(stat, max(dof,1)))
```
On the chain network it agrees with the G-test: `A;C` dependent, `A;C|B`
independent. G and χ² are asymptotically equivalent.

## S2.5 — Mediator vs confounder
Both `X→M→Y` (mediator) and `X←C→Y` (confounder) yield marginal dependence
`I(X;Y)>0` that vanishes when conditioning on the middle variable. A CI test sees
only the *independence pattern*, which is identical for the two structures — they
are **Markov equivalent**. Distinguishing them needs interventions or extra
assumptions, not observational CI tests alone.

## S2.6 — When asymptotics fail
At N=80 with 4 binary conditioners there are up to 16 strata, ~5 samples each, so
many cells have expected count < 5 and the χ² approximation is invalid: p-values
become erratic. A within-stratum permutation test (S6.3) builds the null
empirically and stays calibrated.

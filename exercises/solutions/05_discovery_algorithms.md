# Solutions — Phase 4: Discovery Algorithms

## S5.1 — Trace the phases
Instrument by printing `S` after each add/drop (notebook 04 already narrates
this). On the collider network the grow phase typically adds `A` and `C` first
(strong direct dependence), then `B`/`S` once `C` is present to open the
collider. Whether a drop occurs depends on order; if grow admits a redundant
variable while `S` is incomplete, shrink removes it. Construct an ordering that
forces a drop to see it explicitly.

## S5.2 — Order dependence
Shuffling candidate order across seeds can change *intermediate* states and,
occasionally, the final set on borderline cases. Sorting candidates by
association with `T` (descending) makes the grow phase deterministic and stable,
which is why the notebook does this.

## S5.3 — Inter-IAMB
```python
def inter_iamb(target):
    S = []
    while True:
        cands = [v for v in variables if v != target and v not in S]
        if not cands: break
        best = max(cands, key=lambda x: stat(x, target, S))
        if is_indep(best, target, S): break
        S.append(best)
        # interleaved shrink after each addition:
        for x in list(S):
            rest = [v for v in S if v != x]
            if is_indep(x, target, rest):
                S.remove(x)
    return S
```
Inter-IAMB keeps the maximum conditioning-set size **smaller** than IAMB because
it prunes immediately, improving CI-test reliability on harder problems.

## S5.4 — Count the CI tests
Wrap `g_test` with a counter. IAMB generally uses fewer tests than Grow-Shrink
because its grow phase adds the best candidate directly rather than rescanning.
The gap widens as you add irrelevant variables `E,F,G,...`; plot calls vs #vars
to see the trend.

## S5.5 — Mini-HITON spouse step
Stage 1 (PC): for each `X`, test `X ⊥ T | Sub` over subsets `Sub ⊆` current PC;
keep `X` if it stays dependent across all tried subsets → recovers `{A, C}`
(direct neighbors). Stage 2 (spouses): for the child `C`, test each remaining
variable `Y` for dependence on `T` given `{C}`; `B` and `S` flip to dependent
(collider opened) and are added. Result `{A, C, B, S}`. Stage 2 is exactly what
turns a parents/children finder into a true Markov-Blanket finder.

## S5.6 — Caching with symmetry
Key on `(min(x,y), max(x,y), frozenset(z))`. The symmetric key is valid because
`I(X;Y|Z)=I(Y;X|Z)`, so the test result is order-independent. On a full
Grow-Shrink run the hit rate is modest but non-zero (repeated pairs across grow
and shrink); the benefit grows with problem size and with algorithms that revisit
pairs frequently.

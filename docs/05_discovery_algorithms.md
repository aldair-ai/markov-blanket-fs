# 05 — Discovery Algorithms

All algorithms reach `MB(T)` using a sequence of CI tests. They differ in *how*
they grow the candidate set and *how small* they keep the conditioning set
(which controls CI-test reliability).

## Grow-Shrink (GS) — Margaritis & Thrun, 1999

The original. Two phases:

**Grow.** Start `S = {}`. While some `X` is dependent on `T` given `S`, add it:
```
if not (X ⊥ T | S):  S ← S ∪ {X}
```
**Shrink.** Remove any false positives:
```
if (X ⊥ T | S \ {X}):  S ← S \ {X}
```
Under a perfect CI oracle + faithfulness, the result is exactly `MB(T)`.

*Weakness:* the grow phase can add many variables before shrinking, so `S`
(hence the conditioning set) gets large → CI tests on real data become
unreliable. → `algorithms/grow_shrink.py`

## IAMB — Tsamardinos & Aliferis, 2003

Same two phases, but the grow step adds the variable with the **maximum**
association with `T` given the current blanket. By admitting the most relevant
variable first, the blanket stays small throughout growth, so conditioning sets
stay small and tests stay reliable.
→ `algorithms/iamb.py`

## Inter-IAMB

Interleaves shrink **into** grow: after every single addition, run a shrink
pass. This keeps the candidate blanket minimal at every step — the best
false-positive control of the IAMB family. → `algorithms/inter_iamb.py` (stub)

## HITON-MB — Aliferis et al., 2003

A **local / topology-aware** method. Instead of conditioning on the whole
blanket, it conditions on *subsets*, which is far more sample-efficient:

1. **HITON-PC:** find parents-and-children `PC(T)`.
2. For each `X ∈ PC(T)`, find `PC(X)`; recover **spouses** of `T` (co-parents of
   `T`'s children).
3. `MB(T) = PC(T) ∪ spouses(T)`.

→ `algorithms/hiton_mb.py` (stub)

## MMMB / MMPC — Tsamardinos et al., 2003

Uses the **max-min** heuristic: admit a variable only if its *minimum*
association with `T` over all conditioning subsets is *maximal* — strong control
against false positives. Then recovers spouses like HITON.
→ `algorithms/mmmb.py` (stub)

## How to choose

| Algorithm | Conditioning set | Sample efficiency | Spouses found via |
|-----------|------------------|-------------------|-------------------|
| GS | whole blanket | low | grow+shrink |
| IAMB | whole blanket | medium | grow+shrink |
| Inter-IAMB | whole (kept minimal) | medium-high | grow+shrink |
| HITON-MB | subsets | high | explicit PC step |
| MMMB | subsets | high | explicit PC step |

Rule of thumb: **IAMB** for a solid, simple baseline; **HITON-MB / MMMB** when
you have many variables and limited samples.

## Implementation pitfalls

- **Order dependence.** GS/IAMB results can depend on candidate ordering; sort by
  association for stability.
- **Symmetry correction.** `I(X;Y|Z) = I(Y;X|Z)` — exploit it for caching
  (`utils/caching.py`).
- **Large conditioning sets.** When `|S|` grows, strata become tiny and CI tests
  unreliable; this is the core motivation for the later algorithms.
- **Always validate against known ground truth** (`datasets/synthetic.py`) before
  trusting results on real data.

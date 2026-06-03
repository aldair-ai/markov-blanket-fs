# Exercises — Phase 4: Discovery Algorithms

Prerequisite: `docs/05_discovery_algorithms.md`,
`notebooks/04_grow_shrink_from_scratch.ipynb`.
Solutions in `solutions/05_discovery_algorithms.md`.

## E5.1 — Trace the phases
Instrument `grow_shrink` to print the candidate blanket after every add and
every drop. Run it on the notebook network and identify a concrete case where a
variable added during grow is later removed during shrink (or argue why none is).

## E5.2 — Order dependence
Grow-Shrink can depend on candidate ordering. Run it with candidates shuffled
under several seeds and report whether the final blanket ever changes. Then show
that sorting by association (as in the notebook) stabilizes it.

## E5.3 — Implement Inter-IAMB
Modify IAMB so that a full shrink pass runs *after every single addition*
(interleaved). Compare the maximum conditioning-set size reached by IAMB vs
Inter-IAMB across the grow phase. Which keeps it smaller?

## E5.4 — Count the CI tests
Add a global counter to the G-test. Compare the number of CI tests used by
Grow-Shrink vs IAMB on networks of increasing size (add irrelevant variables
`E, F, G, ...`). Plot calls vs number of variables.

## E5.5 — Implement the spouse step (mini-HITON)
Write a two-stage discoverer: (1) find the parents-and-children set `PC(T)` by
testing each variable against `T` conditioned on subsets of the current PC;
(2) recover spouses by, for each child `C` of `T`, finding variables dependent on
`T` given `{C}`. Verify it recovers `{A, C, B, S}` and explain how stage (2)
finds `B` and `S`.

## E5.6 — Caching with symmetry
Add a cache keyed on `(min(x,y), max(x,y), frozenset(z))`. Report the cache hit
rate during a full Grow-Shrink run and the speedup. Why is the symmetric key
valid?

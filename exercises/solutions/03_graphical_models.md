# Solutions — Phase 2: Graphical Models & d-separation

## S3.1 — d-separation by hand
Network: `A→T→C←S`, `B→C`.
- Given **∅**: `A` and `C` are connected to `T` (not d-separated). `S` and `B`
  reach `T` only through the collider `C`, which is *not* conditioned on, so the
  path is blocked → `S, B` are d-separated from `T`. `D` is disconnected → d-sep.
- Given **{C}**: conditioning on the collider `C` *opens* `S→C←T` and `B→C←T`, so
  `S` and `B` become d-connected to `T`. This matches the CI tests: `S;T`
  independent marginally, dependent given `C`.

## S3.2 — Three path types
| structure | I(X;Y) | I(X;Y\|M) |
|-----------|--------|-----------|
| chain `X→M→Y`   | > 0 | ≈ 0 |
| fork `X←M→Y`    | > 0 | ≈ 0 |
| collider `X→M←Y`| ≈ 0 | > 0 |
Conditioning on `M` **blocks** chains and forks but **opens** colliders.

## S3.3 — Descendant of a collider
With `X→M←Y` and `M→W`, conditioning on `W` partially determines `M`, so it
opens the X–Y path too — weaker than conditioning on `M` directly, because `W` is
a noisy proxy. Consequence: a Markov Blanket must treat descendants of children
carefully; the spouse coupling persists through the child even if you only
observe its effects.

## S3.4 — Factorization and parameter count
`P = P(A)P(B)P(S)P(D)P(T|A)P(C|T,B,S)`.
Free parameters: A,B,S,D = 1 each (4); `T|A` = 2; `C|T,B,S` = 8 → **14** total.
The unrestricted joint over six binary variables needs `2⁶−1 = 63`. The graph
cuts parameters > 4×, the practical payoff of conditional-independence structure.

## S3.5 — Faithfulness violation
Make `Y = X XOR N` with `N` an independent fair bit: then `Y` is marginally
uniform and `I(X;Y)=0` despite the edge `X→Y`. A CI test reports independence and
a discovery algorithm misses the edge. **Faithfulness** is exactly the assumption
that no such cancellation occurs — that every independence in the data reflects a
d-separation in the graph. Deterministic/XOR relations are the classic failure
mode of CI-based methods.

# 04 — Markov Blanket Theory

## Definition

For a target variable `T` in a set of variables `V`, a **Markov Blanket**
`MB(T) ⊆ V \ {T}` is a set that renders `T` conditionally independent of all
other variables:

$$ T \perp\, \big(V \setminus (\{T\} \cup MB(T))\big)\ \big|\ MB(T) $$

A **Markov Boundary** is a *minimal* Markov Blanket (no proper subset is also a
blanket). In practice "Markov Blanket" usually means the minimal one, and under
faithfulness they coincide and are unique.

## Graphical characterization

In a faithful Bayesian network:

$$ MB(T) = \underbrace{\text{parents}(T)}_{\text{direct causes}} \cup \underbrace{\text{children}(T)}_{\text{direct effects}} \cup \underbrace{\text{spouses}(T)}_{\text{co-parents of children}} $$

- **Parents & children** are the obvious neighbors.
- **Spouses** enter through colliders: a child `C` of `T` with another parent `S`
  makes `T` and `S` dependent given `C`. To shield `T` you must include `S`.

The synthetic `collider_network` in this repo is built precisely to exercise the
spouse case.

## The optimality theorem (why we care)

**Claim.** Under faithfulness, `MB(T)` is the optimal feature set for predicting
`T`: conditioned on `MB(T)`, no other variable provides additional information
about `T`.

$$ \forall\, X \notin MB(T)\cup\{T\}:\quad I(T; X \mid MB(T)) = 0 $$

Consequences for feature selection:

- Any predictor that already uses `MB(T)` gains **nothing** from the remaining
  features (in the infinite-data, faithful limit).
- It is **minimal** — every feature in it is necessary; dropping one loses
  information. So MB selection is simultaneously *maximally informative* and
  *non-redundant*. That combination is what makes it principled rather than a
  heuristic like "top-k by mutual information" (which ignores redundancy).

## Uniqueness

Under faithfulness the Markov Boundary is **unique**. Without faithfulness (e.g.
deterministic relations) there can be several minimal blankets, and algorithms
may return any one of them — a caveat to keep in mind on real data.

## From theory to algorithm

The definition gives a brute-force recipe: find the smallest `S` with
`T ⊥ X | S` for all `X ∉ S`. That's exponential. The algorithms in
`05_discovery_algorithms.md` are clever ways to reach the same set with a
polynomial number of CI tests, by growing and shrinking a candidate set.

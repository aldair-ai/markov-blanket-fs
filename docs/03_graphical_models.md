# 03 — Graphical Models & d-separation

## Bayesian networks

A Bayesian network is a **directed acyclic graph (DAG)** plus a conditional
probability distribution per node. It factorizes the joint distribution as

$$ P(X_1,\dots,X_n) = \prod_i P(X_i \mid \text{parents}(X_i)) $$

The graph encodes conditional independencies; the parameters fill in the numbers.

## d-separation — reading independencies off the graph

`d-separation` is the graphical rule that tells you when `X ⊥ Y | Z` holds for
*every* distribution that factorizes over the DAG. A path between X and Y is
**blocked** by `Z` if it contains:

1. a **chain** `A → B → C` or **fork** `A ← B → C` with `B ∈ Z`, or
2. a **collider** `A → B ← C` with `B ∉ Z` **and** no descendant of B in Z.

X and Y are d-separated by Z if **every** path between them is blocked.

### The collider is why spouses exist

At a collider `A → C ← B`, A and B are marginally independent but become
**dependent once you condition on C** (or its descendants). This "explaining
away" is exactly why the Markov Blanket of a target must include the **spouses**
(co-parents of its children): conditioning on the shared child opens a path, so
to block the target off from a spouse you must include that spouse in the
blanket.

This is the single most important graphical fact for MB feature selection, and
the reason a real MB algorithm is more than a parents-and-children finder.

## Faithfulness and the Causal Markov Condition

- **Causal Markov Condition:** every variable is independent of its
  non-descendants given its parents. (Guaranteed by the factorization.)
- **Faithfulness:** *every* independence in the distribution is *implied* by
  d-separation in the graph — there are no "accidental" cancellations creating
  independencies the graph doesn't show.

Under **both**, the Markov Blanket is **unique** and equals

$$ MB(T) = \text{parents}(T)\,\cup\,\text{children}(T)\,\cup\,\text{spouses}(T). $$

All the discovery algorithms assume faithfulness. When it fails (e.g. exact XOR
relationships, deterministic cancellation), CI-based methods can miss edges —
worth knowing when results look wrong on real data.

## Markov Random Fields (undirected)

In an undirected graphical model the Markov Blanket of a node is simply its
**neighbors**. The directed case is richer precisely because of colliders /
spouses. We focus on the directed (BN) view since it matches most causal-feature
-selection settings.

# 02 — Conditional Independence & Testing

## Definition

X and Y are **conditionally independent given Z**, written `X ⊥ Y | Z`, when

$$ P(X, Y \mid Z) = P(X\mid Z)\,P(Y\mid Z) $$

equivalently `P(X | Y, Z) = P(X | Z)`: once you know Z, Y adds nothing about X.

Information-theoretic form (what we actually compute):

$$ X \perp Y \mid Z \iff I(X;Y\mid Z) = 0 $$

## Why it is the heart of MB discovery

The Markov Blanket `MB(T)` is defined by a conditional independence:

$$ T \perp (V \setminus (\{T\}\cup MB(T))) \mid MB(T) $$

So every discovery algorithm is, mechanically, a sequence of CI tests deciding
which variables to add to or remove from a candidate blanket.

## Testing CI from finite data

We never observe `I(X;Y|Z)` exactly — we estimate it and ask whether it is
**significantly** above zero. This is a hypothesis test:

- **H0:** `X ⊥ Y | Z` (independent)
- **H1:** dependent

Decision rule against a significance level α:

| p-value | conclusion |
|---------|------------|
| `> α`   | fail to reject H0 → treat as **independent** |
| `≤ α`   | reject H0 → treat as **dependent** |

### The asymmetry that bites you

"Fail to reject" is **not** proof of independence. With small samples or a large
conditioning set `Z`, the test loses power and wrongly declares independence
(false negative). This is why algorithms that keep `Z` small (IAMB, HITON) are
more reliable than naive Grow-Shrink on real data.

## The tests in this library

| Test | Data | Statistic | Null distribution |
|------|------|-----------|-------------------|
| **G-test** | discrete | `2N·Î(X;Y\|Z)` | χ² with adjusted dof |
| **χ²** | discrete | `Σ(O−E)²/E` | χ² |
| **Fisher's Z** | Gaussian | z-transform of partial correlation | Normal |
| **Permutation (MI)** | discrete | `Î(X;Y\|Z)` | empirical, via within-stratum shuffles |

In a real library these share one `CITest` interface so algorithms are decoupled
from the test. In `notebooks/02_conditional_independence_demo.ipynb` we implement
the **G-test** from scratch (`g_test(x, y, z) -> (statistic, p_value)`) and use it
to decide independence, e.g. checking that `B ⊥ C | A` holds in a chain.

## Degrees of freedom (the subtle part)

For the G/χ² test, the χ² null has

$$ \text{dof} = \sum_{z}(|X_z|-1)(|Y_z|-1) $$

summed over strata of `Z`, using only values that **actually occur** in each
stratum (adjusted dof). Getting this wrong is the most common source of
miscalibrated CI tests. See `06_ci_tests.md`.

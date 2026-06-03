# 01 — Information Theory Foundations

Everything in this library reduces to one question asked over and over:
**does knowing X tell us anything about T once we already know Z?** Information
theory makes that question precise and measurable.

## Entropy — uncertainty in a single variable

$$ H(X) = -\sum_x p(x)\,\log p(x) $$

- Measured in **nats** (natural log) or **bits** (log base 2).
- `H(X) = 0` ⟺ X is constant (no uncertainty).
- Maximal when X is uniform: a fair coin has `H = 1 bit`.

Intuition: the average number of yes/no questions needed to pin down X's value.

## Joint and conditional entropy

$$ H(X,Y) = -\sum_{x,y} p(x,y)\,\log p(x,y) $$
$$ H(X\mid Y) = H(X,Y) - H(Y) $$

`H(X|Y)` is the uncertainty left in X **after** learning Y. Conditioning never
increases entropy: `H(X|Y) ≤ H(X)`.

## Mutual information — shared information

$$ I(X;Y) = H(X) + H(Y) - H(X,Y) = H(X) - H(X\mid Y) $$

- `I(X;Y) ≥ 0`, symmetric.
- `I(X;Y) = 0` ⟺ **X and Y are independent**.
- It's the reduction in uncertainty about X from learning Y (and vice versa).

## Conditional mutual information — the workhorse

$$ I(X;Y\mid Z) = H(X\mid Z) + H(Y\mid Z) - H(X,Y\mid Z) $$
$$ = H(X,Z) + H(Y,Z) - H(X,Y,Z) - H(Z) $$

**This is the central quantity for Markov Blanket discovery:**

$$ I(X;Y\mid Z) = 0 \iff X \perp Y \mid Z $$

In words: given Z, X carries no further information about Y. A Markov Blanket of
T is exactly a set `S` such that `I(T; everything-else | S) = 0`.

The G-test statistic is just a rescaling of an estimate of this:
`G = 2N · Î(X;Y|Z)`.

## Estimation caveats

The plug-in (empirical) estimator is exact for the observed distribution but
**biased upward** for small samples: random fluctuations look like information.
This matters enormously once `Z` is large, because each stratum of `Z` has few
samples. Mitigations:

- Miller–Madow bias correction (`info_theory/estimators.py`).
- Permutation tests for calibrated p-values (`ci_tests/mi_test.py`).
- For continuous data, the KSG k-NN estimator instead of binning.

## Try it

See `notebooks/01_entropy_and_mi.ipynb` and:

```python
from mbfs.info_theory import mutual_information, conditional_mutual_information
```

# Solutions — Phase 0: Information Theory

## S1.1 — Entropy by hand
`H = -Σ p log₂ p = -(0.5·log₂0.5 + 0.25·log₂0.25 + 2·0.125·log₂0.125)`
`= 0.5·1 + 0.25·2 + 0.25·3 = 1.75 bits`. (Verified: `entropy(samples, base=2) ≈ 1.75`.)
It is below 2 bits because the distribution is non-uniform — concentration of
probability mass reduces uncertainty. Entropy is maximal only for the uniform
distribution.

## S1.2 — Chain rule
By definition `H(X,Y) = -Σ p(x,y) log p(x,y)`. Factor `p(x,y)=p(x)p(y|x)`, split
the log, and the first term sums to `H(X)`, the second to `H(Y|X)`. Numerically,
`entropy(x,y)` equals `entropy(x) + (entropy(x,y)-entropy(x))` trivially; the
content is that the second term *is* `H(Y|X)` as defined.

## S1.3 — Symmetry and conditioning
`I(X;Y)=H(X)+H(Y)-H(X,Y)` is symmetric in X,Y by construction.
(a) Chain `A→B→C`: `I(A;C) > 0` but `I(A;C|B) ≈ 0` — conditioning destroys it.
(b) Collider `A→C←B`: `I(A;B) ≈ 0` but `I(A;B|C) > 0` — conditioning creates it.
Both are demonstrated in notebook 01 sections 4–5.

## S1.4 — Data-processing inequality
For `X→Y→Z`, `I(X;Z) ≤ I(X;Y)` because `Z` is a (noisy) function of `Y` and can
only lose information about `X`. Verify by building the chain and comparing the
two MIs. Implication: predicting `X` from the downstream `Z` is never better than
from `Y`; processing cannot add information.

## S1.5 — Miller–Madow
```python
def entropy_mm(*cols, base=None):
    counts = _counts(*cols); n = counts.sum(); p = counts / n
    h = -np.sum(p * np.log(p + (p == 0)))
    h += (np.count_nonzero(counts) - 1) / (2 * n)   # correction (nats)
    return h / np.log(base) if base else float(h)
```
Use it inside an MI estimate `H(X)+H(Y)-H(X,Y)` (correcting each term). On small
samples of an independent pair, the corrected MI sits closer to 0 than the raw
plug-in estimate, which is biased upward.

## S1.6 — Bits vs nats
`I_bits = I_nats / ln 2`. Confirm the ratio is exactly `ln 2 ≈ 0.6931`. Prefer
**bits** for interpretability ("how many yes/no questions") and **nats** for math
(derivatives of `ln` are cleaner; the G-test uses nats).

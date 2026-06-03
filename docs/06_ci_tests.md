# 06 — CI Tests in Depth

The reliability of every MB algorithm is bounded by the reliability of its CI
test. This doc covers the practical statistics.

## G-test = rescaled conditional mutual information

$$ G = 2N \cdot \hat I(X;Y\mid Z) $$

Under H0 (`X ⊥ Y | Z`), `G ~ χ²(dof)`. The p-value is the upper tail. Because
`Î` is biased upward in finite samples, `G` is slightly inflated — more so as
`Z` grows.

## Degrees of freedom (get this right)

$$ \text{dof} = \sum_{z \in \text{strata}(Z)} (r_z - 1)(c_z - 1) $$

where `r_z`, `c_z` are the numbers of values of X and Y that **actually occur**
in stratum `z`. Using the naive `(|X|-1)(|Y|-1)|Z|` over-counts when some
configurations never appear (structural zeros), making the test too
conservative. The adjusted dof in `ci_tests/g_test.py` handles this.

## Sample size and the curse of conditioning

Each variable added to `Z` multiplies the number of strata. With `k` binary
conditioning variables you have `2^k` strata; the data splits thin and counts
per cell collapse. Rules of thumb:

- Aim for **≥ 5 expected count** per cell, or the χ² approximation breaks.
- A common heuristic: require `N ≥ 5 · (#cells)` before trusting a test;
  otherwise **declare independence** (skip the test). This is why minimizing
  `|Z|` (IAMB, HITON) matters so much.

## When asymptotics fail — permutation tests

If cells are sparse, the χ² null is wrong. A **within-stratum permutation test**
(`ci_tests/mi_test.py`) gives a calibrated p-value: shuffle X within each
stratum of Z (preserving `P(X|Z)` and `P(Y|Z)` but breaking the X–Y link) and
compare the observed CMI to the shuffled distribution. Slower but robust.

## Continuous & mixed data

- **Gaussian:** Fisher's Z test on the partial correlation (`fisher_z.py`).
  `X ⊥ Y | Z ⟺ partial correlation = 0` under joint normality.
- **Mixed / nonlinear:** discretize (`utils/discretization.py`, quantile binning)
  then use the G-test, or use a k-NN CMI estimator (KSG). Discretization loses
  information; choose bin count carefully (too many → sparse strata).

## Choosing α

α trades the two error types:

- **Higher α** (e.g. 0.1): more edges admitted → higher recall, more false
  positives in the blanket.
- **Lower α** (e.g. 0.01): stricter → fewer false positives, risk of missing
  true blanket members.

Because each algorithm runs **many** tests, consider that the effective
false-positive rate compounds; some implementations apply a correction, though
the standard MB papers typically use a fixed α and rely on the shrink phase.

## Validation checklist

1. Does the test give `p > α` for genuinely independent pairs in
   `datasets/synthetic.py`?
2. Does it give `p < α` for dependent pairs?
3. Does conditioning on the right variable flip a dependence to independence
   (e.g. `B ⊥ C | A` when B,C are both driven by A)?

`tests/test_ci_tests.py` checks exactly these.

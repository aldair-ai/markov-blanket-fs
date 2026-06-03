# Notebooks

Hands-on companions to the `docs/`. Build them as you learn — each is a place to
*verify the math with code*, which is the fastest way to internalize it.

| Notebook | Goes with | What to build/explore |
|----------|-----------|-----------------------|
| `01_entropy_and_mi.ipynb` | doc 01 | Compute H, MI, CMI by hand vs `mbfs.info_theory`; show `I(X;Y\|Z)=0` for independence; watch small-sample MI bias. |
| `02_conditional_independence_demo.ipynb` | doc 02 | Run `GTest` on dependent/independent pairs; flip a dependence by conditioning; plot p-value vs sample size. |
| `03_markov_blanket_intuition.ipynb` | doc 04 | Build the collider network; show A⊥S marginally but dependent given C → why spouses are in the blanket. |
| `04_grow_shrink_from_scratch.ipynb` | doc 05 | Implement GS step by step, printing the grow/shrink phases; compare with `mbfs.algorithms.GrowShrink`. |
| `05_benchmark_on_known_network.ipynb` | docs 05–06 | Precision/recall vs sample size and α; GS vs IAMB; count CI calls with and without caching. |

Suggested starter for notebook 1:

```python
import numpy as np
from mbfs.info_theory import entropy, mutual_information, conditional_mutual_information

rng = np.random.default_rng(0)
x = rng.integers(0, 2, 5000)
y = x.copy()                      # perfectly dependent
print(entropy(x, base=2), mutual_information(x, y))         # ~1, ~ entropy
z = x.copy()
print(conditional_mutual_information(x, y, z))              # ~0: Z explains all
```

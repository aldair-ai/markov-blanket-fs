"""sklearn-compatible Markov Blanket feature selector.

Wraps the discovery algorithms behind a familiar fit/transform API so the
library drops into any scikit-learn pipeline.

    selector = MarkovBlanketSelector(target="T", algorithm="iamb", alpha=0.05)
    selector.fit(df)
    selector.markov_blanket_      # discovered MB
    selector.transform(df)        # df reduced to the blanket columns
"""
from __future__ import annotations

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from .algorithms import ALGORITHMS
from .ci_tests import get_ci_test
from .utils.caching import CachedCITest


class MarkovBlanketSelector(BaseEstimator, TransformerMixin):
    def __init__(self, target: str, algorithm: str = "grow_shrink",
                 ci_test: str = "g", alpha: float = 0.05, cache: bool = True,
                 ci_kwargs: dict | None = None):
        self.target = target
        self.algorithm = algorithm
        self.ci_test = ci_test
        self.alpha = alpha
        self.cache = cache
        self.ci_kwargs = ci_kwargs or {}

    def fit(self, X: pd.DataFrame, y=None):
        if self.target not in X.columns:
            raise ValueError(f"target {self.target!r} not in DataFrame columns")
        if self.algorithm not in ALGORITHMS:
            raise ValueError(f"unknown algorithm {self.algorithm!r}; "
                             f"choose from {sorted(ALGORITHMS)}")

        ci = get_ci_test(self.ci_test, X, **self.ci_kwargs)
        if self.cache:
            ci = CachedCITest(ci)

        algo = ALGORITHMS[self.algorithm](ci, alpha=self.alpha)
        self.markov_blanket_ = algo.discover(self.target)
        self.ci_ = ci
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        return X[self.markov_blanket_]

    def get_support(self, indices: bool = False):
        cols = list(self.ci_.data.columns)
        mask = [c in set(self.markov_blanket_) for c in cols]
        if indices:
            return [i for i, m in enumerate(mask) if m]
        return mask

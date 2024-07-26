import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class LogScaler(BaseEstimator,TransformerMixin):

    def __init__(self):
        self.n = 4

    def fit(self,x):
        return self

    def transform(self, x: np.ndarray,**kwargs) -> np.ndarray:
        return np.float_power(10, x / (10*self.n))

    def inverse_transform(self, x: np.ndarray,**kwargs) -> np.ndarray:
        return np.log10(x) * 10 * self.n

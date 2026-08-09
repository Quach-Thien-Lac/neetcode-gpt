import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        sum_bce = 0 
        for i in range(len(y_true)):
            sum_bce += y_true[i] * math.log(y_pred[i]) + (1 - y_true[i]) * math.log(1-y_pred[i])
        return round (-1 / len(y_true) * sum_bce, 4)
        pass

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        sum_cce = 0
        sum_cce_term = 0
        for i in range(len(y_true)):
            for j  in range(len(y_true[i])):
                sum_cce_term  += y_true[i][j] * math.log(y_pred[i][j])
            sum_cce += sum_cce_term
            sum_cce_term = 0
        return round ((-1/len(y_true) * sum_cce )+ 1e-7, 4)
        pass


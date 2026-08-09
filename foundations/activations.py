import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        for i in range(len(z)):
            z[i] = round(1 / (1 + math.exp(-z[i])), 5)
        return z
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        for i in range(len(z)):
            z[i] = round(max(0, z[i]), 5)
        return z
        pass

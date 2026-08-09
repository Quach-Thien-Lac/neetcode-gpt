import math
import numpy as np
from numpy.typing import NDArray


class Solution:
    def denomItem(self, largest: np.float64, current: np.float64):
        return math.exp(current - largest)

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        largest = max(z)

        denom = 0
        for i in range(len(z)):
            denom += self.denomItem(largest, z[i])

        for i in range(len(z)):
            z[i] = round(
                self.denomItem(largest, z[i]) / denom,
                4
            )

        return z
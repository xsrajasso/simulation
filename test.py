data = [5, 4, 5, 6, 7, 9, 39, 25, 1, 2, 4, 15]
import numpy as np
from scipy.stats import describe
print(np.mean(data))
print(np.median(data))
print(describe(data))

import numpy as np

x1 = [0, 5, 10]
x2 = [0, 5, 10]
x3 = [10, 5, 0]
x4 = [5, 0, 10]
x5 = [0, 10, 20]
x6 = [3, 7, 1]

correlation = np.corrcoef(x1, x6)
print(correlation)
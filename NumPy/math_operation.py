import numpy as np

random_num = np.random.rand(100)
print("Mean:",np.mean(random_num))
print("Median:", np.median(random_num))
print("Standard deviation:", np.std(random_num))

A = np.array([1, 2, 3, 4, 5])
B = np.array([2, 3, 4, 5, 6])
result = A * B
print("Result:", result)

data = np.array([10, 20, 30, 40, 50])
min_val = np.min(data)
max_val = np.max(data)
normalized = (data - min_val) / (max_val - min_val)
print("Normalized Data:",normalized)
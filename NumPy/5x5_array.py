import numpy as np

a = np.zeros((5, 5))
for i in range(5):
    a[i, i] = 1
print("Identity Matrix:")
print(a)

n = [1,2,3,4,5,6,7,8,9]
arr = np.array(n)
matrix = arr.reshape(3, 3)
print("3X3 Matrix:")
print(matrix)

data = np.array([1,2,3,4,5,6])
data[data % 2 == 0] = -1
print(data)
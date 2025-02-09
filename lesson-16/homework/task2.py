import numpy as np

l1 = [2, 3, 4, 5]
l2 = [1, 2, 3, 4]

@np.vectorize
def square_power(arr):
    return (arr**2)

print(square_power(l1))
print(square_power(l2))
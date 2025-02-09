import numpy as np

li = [32, 68, 100, 212, 77]

# decorator
@np.vectorize
def converter(arr):
    return (arr-32)*5/9

print(converter(li).astype(np.int64))
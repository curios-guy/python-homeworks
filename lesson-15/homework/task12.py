import numpy as np

l1 = np.random.randint(1,10,(3,4))
l2 = np.random.randint(1,10,(4,3))
result = np.dot(l1, l2)
print(result)
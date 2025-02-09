import numpy as np

l1 = np.random.randint(1,10,(3,3))
l2 = np.random.randint(1,10,(3,1))

w = (l1)
y = (l2)
result = np.linalg.solve(w,y)
print(result)
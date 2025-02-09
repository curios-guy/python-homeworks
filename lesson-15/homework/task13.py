import numpy as np

random_mx = np.random.randint(1,10,(3,3))
column_vc = np.random.randint(1,10,(3,1))

result = np.dot(random_mx, column_vc)
print(result)
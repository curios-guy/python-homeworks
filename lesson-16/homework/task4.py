import numpy as np

w = ([
    [10,-2,3],
    [-2,8,-1],
    [3,-1,6]
])

y = ([
    12, -5, 15
])

print(f"l1 = {np.linalg.solve(w,y)[0]}\nl2 = {np.linalg.solve(w,y)[1]}\nl3 = {np.linalg.solve(w,y)[2]}")
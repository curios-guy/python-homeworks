import numpy as np

w = np.array([
    [4,5,6],
    [3,-1,1],
    [2,1,-2]
])

y = np.array(
    [7,4,5]
)

print(f"x = {np.linalg.solve(w,y)[0]}\ny = {np.linalg.solve(w,y)[1]}\nz = {np.linalg.solve(w,y)[2]}")
# output [ 1.7027027   0.62162162 -0.48648649]
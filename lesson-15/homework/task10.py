import numpy as np

main_arr = np.random.randint(1, 10, (4,4))
print(f"Original: \n{main_arr}")
# np.transpose(main_arr)
main_arr.T
print(f"Transpose: \n{main_arr}") 
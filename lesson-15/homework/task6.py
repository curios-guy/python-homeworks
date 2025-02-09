import numpy as np

# generates a random vector of size 30
random_vector = np.random.randint(0, 30, 30)  

# calculates the avrg value
mean_value = np.mean(random_vector)

print("Random Vector:", random_vector)
print("Mean Value:", mean_value)
import math

# main class
class Vector:
    def __init__(self, *components):
        # starts the vector with its components
        if not components:
            raise ValueError("A vector must have at least one component.")
        self.components = components

    def __repr__(self):
        # returns str version of vector
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        # adds two vectors in element
        if not isinstance(other, Vector):
            raise TypeError("Can only add two Vector objects.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to be added.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        # subtracts two vectors
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract two Vector objects.")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to be subtracted.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        # multiplies two vectors with each other
        if isinstance(other, (int, float)):
            # multiplication
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            # dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication is only supported with a scalar or another Vector.")

    def __rmul__(self, other):
        # scalar multiplication from left-hand side
        return self * other

    def magnitude(self):
        # returns a length of a vector
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        # returns a unit vector
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / magnitude for a in self.components))

# usage 
if __name__ == "__main__":
    # create vectors
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    # display the vector
    print(v1)  

    # vector addition
    v3 = v1 + v2
    print(v3)  

    # vector subtraction
    v4 = v2 - v1
    print(v4)  

    # dot product
    dot_product = v1 * v2
    print(dot_product)  # 32

    # scalar multiplication
    v5 = 3 * v1
    print(v5)  

    # magnitude of the vector
    print(v1.magnitude())  

    # normalize the vector
    v_unit = v1.normalize()
    print(v_unit)  
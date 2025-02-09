import numpy as np
import time
l1 = [1, 2, 3, 4]
print([i+2 for i in l1])

l2 = [
    [1,2,3,4],
    [5,6,7,8]
]
# print([[i**2 for i in j] for j in l2])

l3 = ["salom", "asdas", "eqwqe"]
print([len(i) for i in l3])

a1d = np.array([1,2,3,4,5])
# print(a1d)
print(type(a1d))

a2d = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

# print(a2d)

a3d = np.array([
    [
        [1,2,3,4],
        [4,5,6,7]
    ],
    [
        [1,3,4,6],
        [6,3,1,6]
    ]
])

# print(f"\n{a3d}")  
ul = [1,2,3,4,5,6,7, 65897]

a = np.array(ul, dtype = np.int64)
print(a.dtype) #to get info about lists dtypes
# print(type(a))
# print(a)

# range generators 
c = np.arange(10, 15, dtype = np.int32)
print(c)

# generates list in slices
arr = np.linspace(2, 10, 11)
print(arr)

# zeros, (y,x) dimension
zarr = np.zeros((2, 4))
print(zarr)

print(a3d.ndim)

# ones, same aas zeros
ones = np.ones((2,5))
print(ones)
print(ones.dtype)
ones.astype(float) #if we don't define the type of array
# time.sleep(2)
print(ones.dtype)

c = np.array([1, "23"]) #if dtype havent defined
# print(c.dtype)

print(ones * 7) #element - wise multiplication

sevens = np.full((2,7), fill_value = "fsdfs") #fills with given value in given dimension
# print(sevens)

# numpy.empty() is useful when performance is critical, and you plan to overwrite the array's values anyway.
empty = np.empty((2,3), order='F')
# print(empty)

eyearr = np.eye(5,6)
print(eyearr)


# adding / multiplication/ division / subtraction
data = np.array([1,5,8], dtype=np.int64)
oness = np.ones(3,dtype=np.int64)
res = data * oness
print(res)

data2 = np.array(l2, dtype = np.int64)
data3 = np.full((2,4), fill_value=2) 
print("****************")
print(data2)
print(data3)
print(data2 * data3)
print("****************")



"""Broadcasting"""
a1 = np.array([1,2,3], dtype=np.int64) #(1,3)
a2 = np.array([[1], [2], [3], [4]], dtype=np.int64) #(3,1)
print(a1.shape)
print(a2.shape)
print(a1*a2)

print("************************")
"""Multiple uses"""
data4 = np.array([
    [1,2],
    [8,4],
    [5,6]
])
print(data4.max())
print(data4.max(axis = 0)) #top to bottom (could be, not exact )
print(data4.max(axis=1)) #left to right (could be, not exact)
"""max, min elements in 3dimensional arrays"""

data5 = [
    [1,2],
    [4,5],
    [5,6]
]
# data5[1][0]


arr5 = np.array(data5)
print(arr5[1:, 1:]) #only numpy arrays


# getting certain data in list using index [::0, ::1]
#1:28
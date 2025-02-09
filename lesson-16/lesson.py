import numpy as np
from collections import Counter
from PIL import Image

l1 = [
    1,2,3,4,-1,-2,-3,-4,-2,0,0,-2,-4,3,2,0,0,-2
]
a = np.array(l1)

@np.vectorize
def categorize(x):
    if x < 0:
        return 'negative'
    elif x > 0:
        return 'positive'
    elif x == 0:
        return 'zero'

print(categorize(a))

a0 = np.array([1,2,3,4])
a1 = np.array([5,6,7,8])

result = a0 / a1
print(result)

@np.vectorize
def compute_metrics(a,b):
    sum_ab = a + b
    sub_ab = a - b
    return sum_ab, sub_ab

print(compute_metrics(a0, a1))

"""RANDOM"""
cf = np.random.uniform(1, 100, (2,3)).astype(int)
print(cf)
cg = np.random.randint(1,10,(2,3))
print(cg)
cd = np.random.randn()
print(cd)

# choice
values = np.array([10,20,30,40,50])
probabilities = np.array([0.4, 0.1, 0.2, 0.2, 0.1])
vals = np.random.choice(values, size=200, p=probabilities)
print("********************")
print(vals)
print(Counter(vals.tolist()))

# shuffle
arr = np.array([1,2,3,4])
np.random.shuffle(arr)
print(arr)

# *******permutations return new list while shuffle doesnt

# permutations
arr1 = np.array(vals)
permutated = np.random.permutation(arr1)[:4]
print(permutated)

"""linear algebra"""
asd = np.array([[1,2,3,4,5,6,7], [1,2,3,4,5,6,7]])
dsa = np.array([2,3,6,5,3,1,2])

print(np.dot(asd, dsa))
print(asd @ dsa)
print(asd.dot(dsa))

"""IMAGE"""
with Image.open('mount.jpg') as img:
    img_arr = np.array(img)
print(img_arr[0,0])
print(img_arr)

print("********************")
"""turning image to grayscale"""
gray_img_arr = (img_arr[:, :, 0] * 0.299 + img_arr[:, :, 1] * 0.587 + img_arr[:, : , 2] * 0.114).astype(np.int8)
print(gray_img_arr.shape)
print(gray_img_arr)

gray_img = Image.fromarray(gray_img_arr, mode='L')
gray_img.save('mount_grayscaled.jpg')

def save_img(arr,name, mode):
    img = Image.fromarray(arr, mode)
    img.save(f"{name}.jpg")

save_img(gray_img_arr, "mount2", "L")

"""croppping image"""
a0 = 300
a1 = 1700
b0 = 100
b1 = 1000
cropped_img = img_arr[a0:a1, b0:b1, :]
save_img(cropped_img, 'mount_cropped', "RGB")

"""resized image"""
resized_img = img_arr[::2, ::2, :]
save_img(resized_img, 'resized_img', 'RGB')

"""making image shape bigger"""
ix = sorted(list(range(1106)) * 2)
# print(ix)

bigger_img = img_arr[ix][:, ix]
save_img(bigger_img, 'bigger_img', 'RGB')
print(bigger_img.shape)
print(img_arr.shape)
# new_arr = np.random.randint(1, 10, (2, 2))
# asd_inv = np.linalg.inv(new_arr)
# print(asd_inv * asd)


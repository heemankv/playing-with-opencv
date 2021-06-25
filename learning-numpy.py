import numpy as np


mylist = [1, 2, 3]

myarray = np.array(mylist)
print(myarray)


print(np.arange(0, 10))


print(type(np.zeros(shape=(10, 5))))


print(np.ones(shape=(2, 4)))


np.random.seed(101)
arr = np.random.randint(0, 100, 10)

# print(arr)
# arr = np.random.randint(0, 100, 10)
# print(arr)


print(arr.max())
print(arr.min())

print(arr.argmin())

print(arr.mean())

print(arr.reshape(2, 5))


mat = np. arange(0, 100).reshape(10, 10)

print(mat)


row = 4
col = 6

print(mat[row, col])


print(mat[:, 1].reshape(10, 1))


mat[0:3, 0:4] = 0
mynewmat = mat.copy()
print(mynewmat)

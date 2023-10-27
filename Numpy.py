import numpy as np
import pandas as pd

#1. Create a null vector of size 10 but the fifth value which is 1
arr = np.zeros(10)
arr[4] = 1
print(arr)

#2. Create a vector with values ranging from 10 to 49
a = np.arange(10,50)
print(a)

#3. Create a 3x3 matrix with values ranging from 0 to 8
b = np.arange(0,9)
c = b.reshape(3,3)
print(c)

#4. Find indices of non-zero elements from [1,2,0,0,4,0]
c = np.array([1,2,0,0,4,0])
d = np.nonzero(c)
print(d)

#5. Create a 10x10 array with random values and find the minimum and maximum values
arr = np.random.randint(0,101,100)
print(arr.min())
print(arr.max())

#6. Create a random vector of size 30 and find the mean value.
arr = np.random.randint(10,75,30)
mean_arr = np.mean(arr)
print(mean_arr)
import numpy as np
# import pandas as pd

arr = np.array([1, 2, 3, 4, 5]) # 1-D

print(arr)

print(type(arr))

print(arr[1])
print(arr[2] + arr[3])
print(arr[1:5])

a = np.array([[1,2,3,4,5], [6,7,8,9,10]]) #2-D

print("Element on row: ", a[0, 3])

ar = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #3-D

print(ar[1,1 , 2])
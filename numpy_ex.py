
# numpy - numerical python
# numpy operations are speed compared to python lists
# numpy uses less memory compared to python lists
# python lists operations are manual and numpy lists are vectorization
# muti-dimensional lists are difficult in python and very eazy in numpy
import numpy as np

# list1 = np.array([1,2,3,4,5,6])
# print(list1)
#
# list2 = np.array([1,2,3],[4,5,6],[7,8,9])
# print(list2)
# print(list2.ndim)
# print(list2.shape)
# print(list2.size)
# print(list2.dtype)
# print(list2.itemsize)


#Example -5

list1 = np.arange(6)
print(list1)

list2 = list1.reshape(2,3)
print(list2)


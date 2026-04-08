
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

# list1 = np.arange(6)
# print(list1)
#
# list2 = list1.reshape(2,3)
# print(list2)

# list = np.array([1,2,3,4,5])
# print(np.std(list))

# Example - 8 column wise sum and row sum wise
# list = np.array([[1,2,3],
#                  [4,5,6]])
# print(np.sum(list,axis=0)) # column-wise sum
# print(np.sum(list,axis=1)) # row-wise sum

# Example - 9 Broadcasting Example
# list = np.array([10,11,12])
# val = 10
# print(list+val)

# Example - 10
# print(np.random.rand(5)) # 5 elements will generate & range (0-1) the default range
# print(np.random.randint(1,5)) # 1 element & range is (1 - 5)
# print(np.random.rand(3,3)) # 3 X # array will create & range (0-1)

#Example - 11
# list = np.array([10,20,30,40,50])
# print(list[list>=30])

#Example - 12
# list = np.array([3,1,2])
# # print(np.sort(list))
# # print(np.where(list > 1))

#Example - 13
# list1 = np.array([10,20])
# list2 = np.array([20,30])
# list3 = np.concatenate((list1,list2))
# print(list3)
# print(np.split(list3,2))

#Example - 14
list = np.array([[1,2],[3,4]])
print(np.linalg.matrix_transpose(list))
print(np.linalg.inv(list))
print(np.linalg.det(list))

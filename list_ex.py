#Example - 2 - Slicing
# list1 = [10,20,30,40,50]
# print(list1[0],list1[-5])
# print(list1[0:3])
# print(list1[:2])
# print(list1[-3:])
# print(list1[-4:-1])
# print(list1[::-1])

#Example - 3 (Mutability)
# list1 = [1,2,3]
# list1[0] = 100
# print(list1)

#Example - 4 (Add Element)
# list1 = [1,2]
# list1.append(3)
# #print(list1)
#
# list2 = [4,5]
# list1.extend(list2)
# #print(list1)
#
# list1.insert(1,99)
# print(list1)

#Example - 5 (Delete)
# list1 = [1,2,3,2]
# list1.remove(2) # removes first 2
# print(list1)
#
# list1.pop() # removes last element 2
# print(list1)
#
# list1.pop(1) #remove based on index
# print(list1)
#
# list1.clear() #remove all elements
# print(list1)

#Example - 6 (Search of elements)
# list1 = [1,2,3,2,2]
# print(list1.index(2))
# print(list1.index(3))
# print(list1.index(4))

#Example - 7 (Frequency of Elements)
# list1 = [1,2,3,2,2]
# print(list1.count(2))
# print(list1.count(4))

#Example - 8 (Sorting of Elements)
# list1 = [5,2,9,1]
# list1.sort() # mutable
# print(list1) #ascending

# list1.sort(reverse=True)
# print(list1) #decending

# new_list=sorted(list1,reverse=True) #immutable
# print(new_list)
# print(list1)

#Example - 9 (loops)
# list1=[10,20,30,40,50]
# for i in list1:
#     print(i)

# for i in range(len(list1)):
#     print(f'index:{i} and element:{list1[i]}')

#Example - 10
# list1=[i*i for i in range(5)]
# print(list1)
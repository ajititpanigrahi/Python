#Example - 2 - Slicing
# list1 = [10,20,30,40,50]
# print(list1[0],list1[-5]) # o/p - 10 10
# print(list1[0:3]) # o/p - [10, 20, 30]
# print(list1[:2]) # o/p - [10, 20]
# print(list1[-3:]) # o/p - [30, 40, 50]
# print(list1[-4:-1]) # o/p - [20, 30, 40]
# print(list1[::-1]) # o/p - [50, 40, 30, 20, 10]

#Example - 3 (Mutability - we can modify the contents of the element)
# list1 = [1,2,3]
# list1[0] = 100 # o/p - [100, 2, 3]
# print(list1)

#Example - 4 (Add Element)
# list1 = [1,2]
# list1.append(3) # o/p - [1, 2, 3]
# print(list1)
#
# list2 = [4,5]
# list1.extend(list2) # o/p - [1, 2, 3, 4, 5]
# print(list1)
#
# list1.insert(1,99) # o/p - [1, 99, 2, 3]
# print(list1)

#Example - 5 (Delete)
list1 = [1,2,3,2]
# list1.remove(2) # removes first 2 o/p - [1, 3, 2]
# print(list1)
#
# list1.pop() # removes last element 2 o/p - [1, 2, 3]
# print(list1)
#
# list1.pop(1) #remove based on index o/p - [1, 3, 2]
# print(list1)
#
# list1.clear() #remove all elements o/p - []
# print(list1)

#Example - 6 (Search of elements)
# list1 = [1,2,3,2,2]
# print(list1.index(2)) # o/p - 1
# print(list1.index(3)) # o/p - 2
# print(list1.index(4)) # o/p Error ValueError: 4 is not in list

#Example - 7 (Frequency of Elements)
# list1 = [1,2,3,2,2]
# print(list1.count(2)) # o/p - 3
# print(list1.count(4)) # o/p - 0

#Example - 8 (Sorting of Elements)
# list1 = [5,2,9,1]
# list1.sort() # mutable
# print(list1) #ascending o/p -  [1, 2, 5, 9]

# list1.sort(reverse=True)
# print(list1) #decending o/p - [9, 5, 2, 1]

# new_list=sorted(list1,reverse=True) #immutable
# print(new_list) # o/p - [9, 5, 2, 1]
# print(list1)  # o/p - [5, 2, 9, 1]

#Example - 9 (loops)
# list1=[10,20,30,40,50]
# for i in list1:
#     print(i)

# for i in range(len(list1)):
#     print(f'index:{i} and element:{list1[i]}')

#Example - 10
# list1=[i*i for i in range(5)]
# print(list1)
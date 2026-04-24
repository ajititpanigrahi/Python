#Tuple is ordered , immutable , allows duplicates , hetrogeneous, ()
# t1 = (10,20,30)
# print(t1)
# t2 = ('a',10,10.1,"Hello",True,None)
# print(t2)
# t3= ()
# print(t3)
# t4=(10)
# print(type(t4))
# t5=(10,)
# print(type(t5))

#Example - Accessing the tuple elements
# t1 = (10,20,30,40,50)
# print(t1[0],t1[-5])
# print(t1[::-1])
# print(t1[0:2])
# print(t1[0:3])
# print(t1[2:])
# print(t1[:2])

#Example - converting tuple to list
# t1= (10,20,30,40,50)
# list1   = list(t1)
# list1[0]=1000
# t2 = tuple(list1)
# print(t2)

# t1 = (10,20,30,40,50)
# print(t1)
# n = len(t1)
#
# # for i in range(n): # accessing the elements using for loop
# #     print(t1[i])
#
# i = 0
# while i < n:       # accessing the elements using while loop
#     print(t1[i])
#     i += 1

#predefined methods
# t1 = (10,20,30,10,20)
# print(t1.count(10))
# print(t1.index(10))

# unpacking
# nums = (10,20,30,40,50)
# n1 ,n2 ,n3 ,n4 ,n5 =nums
# print(n1,n2,n3,n4,n5)

# nested tuple
# t1 = (
#     (1,"AIML"),
#     (2,"DL"),
#     (3,"GEN AI"),
#     (4,"AGENTIC AI"),
#     (5,"MLOPS")
#     )
# for inner in t1:
#     for element in inner:
#         print(element)

# t1 = (10,20)
# t2 = (30,40)
# t3 = t1 + t2
# print(t3) # concatenation
# print(t3 * 2) # repeat
# print(10 in t3)
# print(100 in t3)
# print(min(t3))
# print(max(t3))
# print(sum(t3))
# print(sorted(t3,reverse=True))
# t4 = tuple([10,20,30,40,50])
# print(t4)

# t1 = (10,[20,30],40)
# list1 = t1[1]
# list1[0] = 2000
# print(t1)

# def test_fun():
#     return (10,3,5,40,50)
# res = test_fun()
# for elements in res:
#      if elements%2 == 0:
#          print(elements)


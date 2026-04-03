#constructor example
# class Student:
#     def __init__(self):
#         self.name="Student1"
#         self.age=20
# s1 = Student()
# print(s1.name)
# print(s1.age)

# constructor initialize Dynamically
#first parameter is always refer to current object
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1=Student("std1", 25)
# print(s1.name)
# print(s1.age)
#
# s2=Student("std2", 30)
# print(s2.name)
# print(s2.age)

#first parameter is always refer to current object it can refer any name but best pratice is
#self as first parameter
# class Test:
#     def __init__(abc, name, age):
#         abc.name = name
#         abc.age = age
# t1=Test("t1", 25)
# print(t1.name)
# print(t1.age)

#Example - 5 use of display function
# class Student:
#     def __init__(self):
#         self.name = "AshokIT"
#     def display(self):
#         print(self.name)
# s1 = Student()
# s1.display()

#Example - 6
# class Demo:
#     def __init__(self  ):
#         self.x = 10 # instance variable
# obj1 = Demo()
# obj1.x = 100
# print(obj1.x)
# obj2 = Demo()
# print(obj2.x)

# Example - 7
# class Demo:
#     x=100 #class variable
# obj1 = Demo()
# obj2 = Demo()
# Demo.x=200
# print(obj1.x)
# print(obj2.x)

#Example - 8
# class Demo:
#     x = 100 #class variable
# obj1 = Demo()
# obj2 = Demo()
# Demo.x = 200
# obj1.x = 300 #instance variable created inside object - obj1
# print(obj1.x)
# print(obj2.x)

#Example - 9
# class Demo:
#     def square(self):
#         num1 = 100
#         res = num1 * num1
#         print(res)
#     def square2(self,num1):
#         res = num1 * num1
#         print(res)
#     def square3(self):
#         num1 = 100
#         res = num1 * num1
#         return res
#     def square4(self,num1):
#         res = num1 * num1
#         return res
# obj = Demo()
# obj.square()
# obj.square2(100)
# res=obj.square3()
# print(res)
# res1=obj.square4(100)
# print(res1)

# Example - 10
# class Demo:
#     x = 100
#     @classmethod
#     def test_method(cls):
#         print(cls.x)
# Demo.test_method()
# obj = Demo()
# obj.test_method()

# Example - 11
# class Demo:
#     @staticmethod
#     def validation(email):
#         return "@" in email
# print(Demo.validation("info@ashokit.in"))

#Exmple - 12
class parent:
    def __init__(self):
        self.x = 200
class child(parent):
    def __init__(self):
        super().__init__() #we need to call the parent class constructor explicitly
        self.y = 300
obj = child()
print(obj.x)
print(obj.y)







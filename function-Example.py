# def test_func(num1, num2):
#     return num1 + num2, num1 - num2, num1 * num2, num1 / num2
#
# addition, subtraction, multiplication, division = test_func(200, 100)
# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)

# def test_fun():
#     return
# x = test_fun()
# print(x)

#local variable
# def test_fun():
#     num1 = 200
#     print(num1)
#
# test_fun()
# print(num1)

#global variable
# num1 = 200
# def test_fun():
#     print(num1) #200
#
# test_fun()
# print(num1) #200

# num1 = 200
# def test_fun():
#     num1 = 100
#     print(num1) #100 local variable value
# test_fun()
# print(num1) # 200 global variable value

num1 = 200
def test_fun():
    global  num1
    num1 = num1 + 100

test_fun()
print(num1)



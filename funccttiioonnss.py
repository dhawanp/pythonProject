'''
Functions are piece of reusable code , that can be used again and again in a program , rather than writing the same code
over and again
There are 2 different types of funtions-:
1.). Built-in functions
2.). USer Defined functions

Parameters act as an input to the function while calling the function
'''

# def squary(n):
#     print(f"the number provided by user to be squared is-{n}")
#     result=n*n
#     # print(f"The sqaure of the user entered number is {result}")
#     return result
#
# n=int(input("Enter the number which is to be squared upon-:"))
# var=squary(n)
# print(var)

'''
RETURN STATEMENT
Default return value of a function is none
'''


'''
FUNCTION ARGUMENTS

It is the actual value of any variable which is passed to the function

Types of Arguments-:1. Default
2. keyword(Mention their names and specify their value as well)
3. Positional(Position of an argument)
4. Variable Length(A function which can take any number of arguments or n number of arguments(User *args in the parameters of a function definition)
'''

'''
DECORATORS

A function as an argument to another function is called as a decorator
'''
# def decor_sum(func):
#     def dec(x,y):
#         print('#'*20)
#         print("Sum:",end='')
#         func(x,y)
#         print('#'*20)
#     return dec
#
# @decor_sum
# def add(a,b):
#     print(a+b)
#
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# add(a,b)
# sum1=decor_sum(add)
# print(sum1)

'''
Interview Questions
'''
def funcy(*x ,y):
    print(x)
    print(y)
# funcy(1,2) #Will Throw Error
# funcy(1,2,3,4,5,6,7,8,9) #Will Throw Error
funcy(1,y=2)
funcy(1,2,3,4,5,6,7,8,y=9)
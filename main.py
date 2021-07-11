# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Peter's sister's name's "Anna"

# print('Peter\'s sister\'s name\'s \"Anna\"')
#
# print(2 ** 3 ** 2 ** 1)
#
#
# i = 250
# while len(str(i)) > 72:
#  i *= 2
# else:
#  i //= 2
# print(i)
#
# n = 0
# while n < 4:
#  n += 1
#  print(n,end=" ")
#  #print(n)
#
# a = 0
# b = a ** 0
# if b < a + 1:
#     c = 1
# elif b == 1:
#     c = 2
# else:
#     c = 3
# print(a + b + c)
#
# lst = []
# n = int(input("Enter number of elements : "))
#
# for i in range(0, n):
#     ele = input(), int(input())
#     lst.append(ele)
#
# print(lst)
#
# print("I'm", '\""learning\""' , '\"""Python\"""' ,sep="\n")

'''

nolocal keyword is used inside a nested function in-order to define that the variable used inside the nested/inner function is not local
'''

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())




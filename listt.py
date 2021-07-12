# '''
# LISTS are MUTABLE(C--->Create Yes
#                      R---> Read Yes
#                      U--->Update Yes
#                      D--->Delete Yes)
# '''
# from random import random
#
# list=[2,7,1,4,6,9,0]
# print(list)
# print(sorted(list))
# list.append("chaumau")
# print(list)
# list.insert(0,33)
# print(list)
# (list.remove(33))
# print(list)
# '''
# POP
# If the argument is not passed then by default it removes the last element that is a list[-1]
# The pop() method removes the item at the given index from the list and returns  the removed item.
# '''
# print(list.pop(0))
# print(list)
# print(id(list))
# a=[1,2,3,4,5]
# a.extend([6,7,8,9])
# print(a)
# alphabet = ['a', 'b', 'c']
# integers = [1, 2, 3]
#
# """
# List Slicing
# """
#
# b=[1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
# print(b[3:8])
# print(b[:10])
# print(b[0:12:1])
# print(b[:12:3])
#
# #Return every 2nd element in a list between 2 indices
# li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
# print(li[10:16:2])
#
# #Sort a list of integers in ascending order
# li2 = [10,1,9,2,8,3,7,4,6,5]
# li2.sort()
# print(li2)
#
# #Sort a list of integers in descending order
# li = [10,1,9,2,8,3,7,4,6,5]
# li.sort(reverse=True)
# print(li)
#
# # sorting using custom key
#
# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]
# def get_age(employees):
#     return employees.get('age')
#
# employees.sort(key=get_age)
# print(employees)
#
# def get_name(employees):
#     return employees.get('Name')
#
# employees.sort(key=get_name)
# print(employees)
#
# '''
# swap the first and the last element of a list
# '''
# list3=[12,35,9,56,24]
# tmp=list3[4]
#
# list3[4]=list3[0]
# list3[0]=tmp
# print(list3)


'''
Program to create a list dynamically , and swap the first and the last elements
'''

# li4=[]
# n=int(input("Enter the number of elements to be inserted in the list:"))
# for i in range(n):
#     ele=input(),int(input())
#     li4.append(ele)
# print(li4)
#
# size=len(li4)
# print(size)
# li4[0] , li4[size-1] = li4[size-1] ,li4[0]
# print(li4)
#
#
# li5=[23,13,45,11,10,9,7,5,4,100]
# li5.sort()
# print(li5)
#
# li6=[]
# n=int(input("Enter the number of elements to be included in the list:"))
#
# for i in range(0,n):
#     ele=int(input())
#     li6.append(ele)
# print(li6)
#
#
# for j in range(len(li6)):
#     min1=li6[0]
#     if li6[j]<min1:
#         min1=li6[j]
# print(min1)
#
'''
Program to find the occurrence of a digit in a particular list
'''
# li7=[]
# n=int(input("Enter the number of elements to be included in the list-"))
# for i in range(n):
#     ele=int(input())
#     li7.append(ele)
# print(li7)
#
# m=int(input("Enter the digit for which you want to check the occurrence:"))
# count=0
# for i in li7:
#     if i == m:
#         count+=1
# print(count)
'''
Using the list() constructor to make a List
'''
# thislist = list(("apple", "banana", "cherry","pine"))
# print(thislist)
# li=[9,7,5,3,1,2,4,6,8,0]
# #print(sorted(li))
# li.sort()
# print(li)
# li.remove(8)
# print(li)
# li.pop(4)
# print(li)
# li.insert(3,"abc")
# print(li)
# #li.sort()
# print(li)
# '''
# Removal of other elements from a list and adding some other elements in the same list
# In this example If I would have used li[1:2]=[99,100] , it would have just replaces element at index 1 , but on using li[1:4]=[99,100] , it removed
# element at index 1 ,2,3 and inserted 99 , 100 values there
# '''
# li[1:4]=[99,100]
# print(li)
'''
Program to swap first and the last elemnts in a list
'''
# li9=[]
# n=int(input("Enter the number of elements to be included in the list"))
# for i in range(n):
#     elements=int(input())
#     li9.append(elements)
# print(li9)
# size=len(li9)
# li9[0] , li9[size-1] = li9[size-1] , li9[0]
# print(li9)

# NORMAL LIST FEATURES AND FUNCTIONALITIES
li10=[1,2,3,4,5,6,7,8,9]
print(li10)
li10.append(10)
print(li10)
li10.insert(3,33)
print(li10)
li10.insert(5,33)
print(li10)
li10.remove(33) #Notice how remove() removes just the first match of the object it is trying to remove
print(li10)
print(li10)
li10.insert(3,77)
print(li10)
print(li10.pop(3))
print(li10)
li10.append(77)
print(li10)
del li10[10]
print(li10)



'''
LISTS are MUTABLE(C--->Create Yes
                     R---> Read Yes
                     U--->Update Yes
                     D--->Delete Yes)
'''
from random import random

list=[2,7,1,4,6,9,0]
print(list)
print(sorted(list))
list.append("chaumau")
print(list)
list.insert(0,33)
print(list)
list.remove(33)
print(list)
list.pop(0)
print(list)
print(id(list))
a=[1,2,3,4,5]
a.extend([6,7,8,9])
print(a)
alphabet = ['a', 'b', 'c']
integers = [1, 2, 3]

"""
List Slicing
"""

b=[1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
print(b[3:8])
print(b[:10])
print(b[0:12:1])
print(b[:12:3])

#Return every 2nd element in a list between 2 indices
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
print(li[10:16:2])

#Sort a list of integers in ascending order
li2 = [10,1,9,2,8,3,7,4,6,5]
li2.sort()
print(li2)

#Sort a list of integers in descending order
li = [10,1,9,2,8,3,7,4,6,5]
li.sort(reverse=True)
print(li)

# sorting using custom key

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
def get_age(employees):
    return employees.get('age')

employees.sort(key=get_age)
print(employees)

def get_name(employees):
    return employees.get('Name')

employees.sort(key=get_name)
print(employees)

'''
swap the first and the last element of a list
'''
list3=[12,35,9,56,24]
tmp=list3[4]

list3[4]=list3[0]
list3[0]=tmp
print(list3)


li4=[]
n=int(input("Enter the number of elements to be inserted in the list:"))
for i in range(n):
    ele=[input(),int(input())]
    li4.append(ele)
print(li4)

size=len(li4)
li4[0] , li4[size-1] = li4[size-1] ,li4[0]
print(li4)


li5=[23,13,45,11,10,9,7,5,4,100]
li5.sort()
print(li5)

li6=[]
n=int(input("Enter the number of elements to be included in the list:"))

for i in range(0,n):
    ele=int(input())
    li6.append(ele)
print(li6)


for j in range(len(li6)):
    min1=li6[0]
    if li6[j]<min1:
        min1=li6[j]
print(min1)

'''
Program to find the occurrence of a digit in a particular list
'''
li7=[]
n=int(input("Enter the number of elements to be included in the list-"))
for i in range(n):
    ele=int(input())
    li7.append(ele)
print(li7)

m=int(input("Enter the digit for which you want to check the occurrence:"))
count=0
for i in li7:
    if i == m:
        count+=1
print(count)

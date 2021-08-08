'''
TUPLES are IMMUTABLE(C--->Creates Yes
                     R---> Read Yes
                     U--->Update No
                     D--->Delete No)
'''

# tuple1=(1,2,3,4,5,6,7,'Prateek',12.7,'!','@')
# print(tuple1)
#We can have a list inside a tuple , but we can not modify any element of the list as this would break clause of tuple being
#immutable

# n=int(input())
# print(n*2,"\n")
# str1=input()
# print(str1)


'''
Tuple PACKING
'''
a=1.5,2,3,'PRATEEK'
print(type(a))
print(a)


'''
TUPLE UNPACKING
'''
b,c,d,e=a
print(b,c,d,e)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruity = ("apple", "banana", "cherry", "strawberry", "raspberry")

(blue, turq, *lavendar) = fruity

print(blue)
print(turq)
print(lavendar)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(red, *brown, peach) = fruits

print(red)
print(brown)
print(peach)
# '''
# Conversion of a Tuple into a List
# '''
#
# tuple2=1,2,3,4.7,'PRATEEK'
# print(type(tuple2))
# print(tuple2)
# list2=list(tuple2)
# print(type(list2))
# print(list2)
#
#
# '''
# Conversion of a List into a Tuple
# '''
#
#
# list3=[1,2,3,4,5,'PRATEEK','!','@','#']
# print(type(list3))
# print(list3)
# tuple3=tuple(list3)
# print(type(tuple3))
# print(tuple3)

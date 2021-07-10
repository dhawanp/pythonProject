# list=[2,7,1,4,6,9,0]
# print(list)
# print(sorted(list))
# list.append("chaumau")
# print(list)
# list.insert(0,33)
# print(list)
# list.remove(33)
# print(list)
# list.pop(0)
# print(list)
# print(id(list)) #The id is the object's memory address, and will be different for each time you run the program
# a=[1,2,3,4,5]
# a.extend([6,7,8,9])
# print(a)
# # alphabet = ['a', 'b', 'c']
# # integers = [1, 2, 3]
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

# a="NITIN"
# print(a[::-1])
# if a[::-1] == a:
#     print("yes it is a palindrome")

a=input("Enter the string for which you want to test it as a palindrome or not-:")
if a[::-1] == a:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")

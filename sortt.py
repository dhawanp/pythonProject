li1 = []
num = int(input("Enter the number of elements you want-:"))
for i in range(num):
    elements = int(input())
    li1.append(elements)
print(li1)
li2 = []
while li1:
    min = li1[0]
    for i in li1:
        if i < min:
            min = i
    li2.append(min)
    li1.remove(min)
print(li2)
li3 = li2
li4 = []
for i in li3[:]:
    if i == 0:
        li3.remove(i)
        li4.append(i)
print(li4)
result = li3 + li4
print(result)


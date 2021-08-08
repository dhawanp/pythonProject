a=1

while a<10:
    print(a)
    a += 1
    if(a==5):
        break

    else:
        print("Out of the while loop")

'''
for loop iterates over a sequence of items
'''
li1=[1,2,3,4,5,6]
sum=0
avg=0
for i in li1:
    print(i)
    sum=sum+i
    print(sum)
avg=sum/len(li1)
print(avg)
# for loop using range()
for i in range(0,10):
    print("i:%d"%i)
# for loop using range() with step count
for i in range(0,10,2):
    print("i:%d"%i)
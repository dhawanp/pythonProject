#Program TO PRINT THE FIBONNACI SERIES
a=0
b=1
count=0
num=int(input("Enter the number of terms for which you want fibonnaci series-:"))
if num<0:
    print("Please ENTER THE POSITIVE NUMBER OF TERMS-:")
elif num==1:
    print("The Fibonnaci Series is-:",a)
else:
    while count<num:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
'''
If else and elif are used for decision making
'''

marks=int(input("Enter the marks obtained by the student-"))
subject=input("Enter the subject-")
standard=int(input("Enter the class/grade/standard-"))
school=input("Enter the name of the school")

if(marks>88):
    print("A++")
    if(subject=="ENG"):
        print("subject entered is English")
        if standard<7:
            print("KID")
            if(school=="MSMS"):
                print("School is MSMS")
            else:
                print("School isn't MSMS")
        else:
            print("Not a KID")
            if(school=="ABCD"):
                print("School is ABCD")
    else:
        print("Not Good MArks yaar , try more harder")
        if(standard<2):
            print("Small KID")
        else:
            print("Big KID")
            if(standard==9):
                print("Very Big KID")

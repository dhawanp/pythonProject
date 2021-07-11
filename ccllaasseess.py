# class Person:
#     def __init__(self,nome,aged):
#         self.name=nome
#         self.age=aged
#     def dispPerson(self):
#         print(f"Name of the person is-:{self.name}")
#         print(f"The age of the person is-:{self.age}")
#
# name=input("enter the name of the person:")
# agey=int(input("Enter the age of the person:"))
#
# p1=Person(name,agey)
# p1.dispPerson()

class Base:
    def __init__(self,nome,roll,stand):
        self.name=nome
        self.rollnumber=roll
        self.standard=stand
    def dispStudentInfo(self):
        print("==============NOW DISPLAYING=========================")
        print(f"The name of the student is: {self.name}")
        print(f"The roll number of the student is: {self.rollnumber}")
        print(f"The standard in which student is studying is: {self.standard}")
obj1=[]
nos=int(input("Enter the number of students for which you want to store the record:"))
for i in range(nos):
    rollcall=int(input("Enter the roll number of the student:"))
    nomenclature=input("Enter the name of the student:")
    stan=int(input("Enter the standard in which student is studying:"))
    obj1.append(Base(nomenclature,rollcall,stan))
for j in range(nos):
    print(f"Tne information about student {j+1} is")
    obj1[j].dispStudentInfo()

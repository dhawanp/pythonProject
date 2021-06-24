class Student:
    '''This is a Class Level Documentation'''
    #Variable
    #Method
print(Student.__doc__)

'''
Object Is The Physical Implementation of the Class
Objects are stored in reference variable
'''
# class Student:
#     def input(self):
#         roll=int(input("Enter the Roll Number:"))
#         name=input("Enter the name of the student:")
#         standard=int(input("Enter the standard in which student is studying:"))
#         print(roll)
#         print(name)
#         print(standard)
# st1=Student()
# st1.input()
'''
Self keyword in above code is used to represent the current object
'''

'''
The First method to be executed when the object is created is Constructor
The main purpose of the constructor is to initialize the instance variable
The name of the constructor starts from __init__(self)
self variable points to current object of the class
'''
class Student:
    def __init__(self,roll,name,standard):
        print("Address of the \"Self\" Variable is",id(self))
        self.rollnumber=roll
        self.name=name
        self.stan=standard
    def dispMarks(self):
        print(f"The Roll Number of the Student is :{self.rollnumber}")
        print(f"The Name of the Student is:{self.name}")
        print(f"The Standard of the student is:{self.stan}\n")
# st1=Student(int(input("Enter the Roll number:")),input("Enter the Name of the Student:"),int(input("Enter the Standard:")))
# print("Address of the object pointing to student class is:",id(st1))
# st1.dispMarks()


obj1=[]
nos=int(input("Enter the number of records of students which you would like to feed into the system:"))
for i in range(nos):
    roll=int(input("Enter the roll no.:"))
    name=input("Enetr the name of the student:")
    standard=int(input("Enter the standard:"))
    obj1.append(Student(roll,name,standard))
for j in range(nos):
    obj1[j].dispMarks()
'''
Inheritance and super keyword
'''
class Base:
    def __init__(self,name,age):
        print("This is a parent class constructor")
        self.name=name
        self.age=age
        print(f"Name={self.name},age={self.age}")
    def method1(self):
        print("This is parent class dummy method")
class Derived(Base):
    def __init__(self,name,age):
        print("This is child class's constructor method")
        super().__init__(name,age)
    def method2(self):
        print("This is a child class dummy method")
d=Derived('PRATEEK',16)
d.method1()
d.method2()


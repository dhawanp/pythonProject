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
        print(f"The Standard of the student is:{self.stan}")
st1=Student(int(input("Enter the Roll number:")),input("Enter the Name of the Student:"),int(input("Enter the Standard:")))
print("Address of the object pointing to student class is:",id(st1))
st1.dispMarks()
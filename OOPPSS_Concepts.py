class Student:
    '''This is a Class Level Documentation'''
    #Variable
    #Method
print(Student.__doc__)

'''
Object Is The Physical Implementation of the Class
Objects are stored in reference variable
'''
class Student:
    def input(self):
        roll=int(input("Enter the Roll Number:"))
        name=input("Enter the name of the student:")
        standard=int(input("Enter the standard in which student is studying:"))
        print(roll)
        print(name)
        print(standard)
st1=Student()
st1.input()
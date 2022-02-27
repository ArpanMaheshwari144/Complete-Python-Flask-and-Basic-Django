class Student:
    clg="xyz"  #class varaible

    def __init__(self,srollno,sname):
        self.rollno=srollno  #instance variable
        self.name=sname      #instance variable

    def display(self):
        print("Student Name:",self.name)
        print("Student Roll Number:",self.rollno)
        print("College is:",self.clg)

student1=Student(1,"Arpan")
print(student1)
student1.display()

student2=Student(2,"Adarsh")
print(student2)
student2.display()

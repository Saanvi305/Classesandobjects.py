#creating a class 

class Student():
    #properties/attributes
    name=""
    age=12
    schoolclass="6th A"
    house="Saphire"
    classteacher="Poonam Ma'am"

    #constructor
    def __init__(self):
        print("Making a new student")


    #Another function
    def change_details(self):
        print ("please enter your age: ")
        self.age = int (input())
        print("Please enter the name of the student")
        self.name=input()
              
    #Another function
    def show_Details(self):
        print("The details of student are:")
        print("Name : " ,self.name)
        print("Age : " ,self.age)
        print("Class: " ,self.schoolclass)
        print("House : " ,self.house)
        print("Class teacher name :,self.classteacher")

    #Student class definition is over
    #MakiNg 2 objects/instances of Student class 
Shivika=Student()
Saanvi=Student()
Shivika.change_details()
Saanvi.show_Details()







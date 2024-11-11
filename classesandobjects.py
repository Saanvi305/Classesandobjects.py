import math 
#define a class named Circle
class Circle:
    #constructor to initialise the radius:
    def __init__(self,radius):
      self.radius=radius
    #Methods to calculate area and circumference 
    def calculate_area(self):
        areaR=math.pi*self.radius
        return areaR
    #method to calculate the circumference 
    def circumference(self):
        circumf=2*math.pi*self.radius
        return circumf
    

#create an object of the circle
mycircle=Circle(5)
area=mycircle.calculate_area()
circumference=mycircle.circumference()
print("The area of the circle is ", area)
print("The circumference of the circle is" ,circumference)


#Define a class named student 
class Student:
    #constructor to initialise attributes
    def __init__(self, name, grade):
       self.name=name             #Attribute for the students name
       self.grade=grade            #Attribute for the students grade
       
    
    #Method to display students details 
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")

#Create an object of the studant class
Student1= Student ("John","A")

Student1.display_info()


       

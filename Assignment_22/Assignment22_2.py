# Write a Python program to implement a class named Circle with the following requirements

class Circle:
    Pi = 3.14

    def __init__(self):
        print("inside constructor")
        self.Radius = 0.0
        self.Area= 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius : " ))

    def CalculateArea(self):
        self.Area = Circle.Pi * self.Radius ** 2
        

    def Calculate_Cicumference(self):
        self.Circumference = 2 * Circle.Pi * self.Radius

    def Display(self):
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circumference)
    
obj1 = Circle()
obj2 = Circle()


obj1.Accept()
obj1.CalculateArea()
obj1.Calculate_Cicumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.Calculate_Cicumference()
obj2.Display()


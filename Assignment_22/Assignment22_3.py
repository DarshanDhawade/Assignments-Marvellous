# Write a Python program to implement a class named Arithmatic with the following characyeristics

class Arithmatic:
    Value1 = (None)
    Value2 = (None)

    def __init__(self):
        print("inside constructor")
        Arithmatic.Value1 = 0
        Arithmatic.Value2 = 0
        

    def Accept(self):
        Arithmatic.Value1 = int(input("enter number : "))
        Arithmatic.Value2 = int(input("enter number : "))

    def Addition(self):
        ans = Arithmatic.Value1 + Arithmatic.Value2
        print("Addition is  :" ,ans)
        

    def Subtraction(self):
        ans = Arithmatic.Value1 - Arithmatic.Value2
        print("Substraction is  :",ans)

    def Multiplication(self):
        ans = Arithmatic.Value1 * Arithmatic.Value2
        print("Multiplication is  :", ans)

    def Division(self):
        ans = Arithmatic.Value1 / Arithmatic.Value2
        print("Division is :", ans)


obj1 = Arithmatic()
obj2 = Arithmatic()


obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()

obj2.Accept()
obj2.Addition()
obj2.Subtraction()
obj2.Multiplication()
obj2.Division()


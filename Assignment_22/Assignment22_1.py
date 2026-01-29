# Write a Python program to implement a class named demo with the following specifications 

class Demo:
    Value = 10

    def __init__(self,i,j):
        print("inside constructor")
        self.no1 = i
        self.no2 = j

    def fun(self):
        print("inside instance method fun : " , self.no1, self.no2)

    def gun(self):
        print("inside instance method gun : " , self.no1, self.no2)

    @classmethod
    def sun(cls,value):
        print("inside class method sun")

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()
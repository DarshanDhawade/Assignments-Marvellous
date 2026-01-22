# Write a program which accepts radius of a circle and prints area of a circle

import math

def RadiusofC():

    Radius = int(input("Enter Radius : "))

    Area = math.pi * Radius **2

    print("Area of the circle is : " , Area)

def main():
    RadiusofC()

if __name__=="__main__":
    main()
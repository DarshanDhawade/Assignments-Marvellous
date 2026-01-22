# Write a program which accepts length and width of rectangle and prints area

def AofRect():
    Length = int(input("Enter Length of Rectangle : "))
    Width = int(input("Enter width of Rectangle : "))

    Area = Length * Width
    print("Area of Rectangle : " , Area)

def main():
    AofRect()

if __name__=="__main__":
    main()
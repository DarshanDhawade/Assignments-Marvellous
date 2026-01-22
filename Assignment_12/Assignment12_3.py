# Write a program which accepts two number and prints their addition subtraction multiplication division

def AriOperations():
    No1 = int(input("Enter Number 1 : "))
    No2 = int(input("Enter Number 2 : "))

    Addition = No1 + No2
    print("Addition is :", Addition)

    Subtraction = No1 - No2
    print("Subtraction is :", Subtraction)

    Multiplication = No1 * No2
    print("Multiplication is :", Multiplication)

    Division = No1 / No2
    print("Division is :", Division)

def main():
    AriOperations()

if __name__=="__main__":
    main()
# Write a program which accept number from user and check whether that number is positive or negative or zero

No = int(input("Enter Number : "))

def Check():
    if No > 0:
        print("Positive")
    else :
        print("Negative")

def main():
    if No == 0:
        print("zero")
    else: Check()


if __name__=="__main__":
    main()
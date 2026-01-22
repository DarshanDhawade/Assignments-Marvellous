# Write a program which accepts one number and checks whether it is palindrome or not

def Palindrome():
    No = int(input("Enter Number : "))
    ActualNo = No

    Reverse = 0

    while No > 0:
        Dig = No % 10
        Reverse = Reverse * 10 + Dig
        No = No // 10

    if ActualNo == Reverse:
        print("Is a Palindrome")
    else:
        print("Is not a Palindrome")

def main():
    Palindrome()


if __name__=="__main__":
    main()
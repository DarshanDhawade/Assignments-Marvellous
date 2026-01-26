# Write a program which accepts one number from user and returns sum of digits of that number 

def SumDig():
    No = int(input("Enter your Number : "))
    Sum = 0

    while No > 0:
        digit = No % 10
        No = No // 10
        Sum = Sum + digit
    print(Sum)

def main():
    SumDig()
   

if __name__=="__main__":
    main()
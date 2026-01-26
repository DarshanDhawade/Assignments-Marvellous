# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 or else false

def DivisibleBy5(No):
     return No % 5 == 0

def main():
    No = int(input("Enter Number : "))
    result = DivisibleBy5(No)
    print(result)
    
if __name__=="__main__":
    main()
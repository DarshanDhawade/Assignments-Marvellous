# Write a program which contains one function named as ChkNum() which accepts one parameter as number.
# If number is even then it should Display "even number" otherwise display "odd number" on console 

def ChkNum():
    No = int(input("Enter number : "))
    if No % 2 == 0:
        print("Even Number ")
    else :
        print("Odd Number ")

def main():
    ChkNum()

if __name__=="__main__":
    main()
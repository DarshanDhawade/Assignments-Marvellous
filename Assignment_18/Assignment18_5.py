# Write a program which accepts N number from user and store it into list
# Retrun addition of all prime number from list main python file accepts N number from user and pass each number to ChkPrime()
# 
import MarvellousNum

def ListPrime(Numbers):
    Sum = 0

    for i in Numbers:
        if MarvellousNum.ChkPrime(i):
            Sum += i
    return Sum

def main():
    No = int(input("Enter Count : "))
    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)
    print(Numbers)

    result = ListPrime(Numbers)
    print("sum of prime numbers :" , result)
    
if __name__=="__main__":
    main()
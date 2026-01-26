# Write a program which accept one number from user and return addition of its factors

def FactorSum():
    No = int(input("Enter Number : "))
    sum = 0
    for i in range(1, No + 1):
        if No % i == 0:
            sum  +=  i
        print(sum)
            
def main():
    FactorSum()

if __name__=="__main__":
    main()
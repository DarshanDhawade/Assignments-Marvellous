# Write a program which accepts one number and prints its factors

def Factors():
    No = int(input("Enter Number : "))

    for i in range(1, No + 1):
        if No % i == 0:
            print(i)

def main():
    Factors()

if __name__=="__main__":
    main()
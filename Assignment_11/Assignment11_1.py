# Write a program which accepts one number and checks whether it is prime or not

def CheckPrime():
    No = int(input("Enter Number : "))

    if No <= 1:
        print(No,"is not Prime")
    else:
        CheckPrime = True
        for i in range(2,No):
            if No % i == 0:
                CheckPrime = False
                break

        if CheckPrime:
            print(No," is Prime")
        else :
            print(No," is not Prime")
 
def main():
    CheckPrime()

if __name__=="__main__":
    main()
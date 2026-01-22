# Write a program which accepts one number and checks whether it is perfect or not

def CheckPerf():
    No = int(input("Enter Number : "))
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = i + i
            

    if sum == No:
        print(No,"is perfect number")
    else :
        print(No,"not a perfect number") 


def main():
    CheckPerf()

if __name__=="__main__":
    main()
# Write a program which accepts one number and checks whether it is divisble by 3 and 5

def Check3_5():
    No = int(input("enter number : "))
    if No % 3 == 0 and  No % 5 == 0 :
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    Check3_5()


if __name__=="__main__":
    main()
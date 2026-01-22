# Write a program which accepts one number and returns reverse of that number
def Reverse():
    No = int(input("Enter Number : "))

    Reverse = 0

    while No > 0:
        dig = No % 10
        Reverse = Reverse * 10 + dig
        No = No // 10
    print(Reverse)

def main():
    Reverse()

if __name__=="__main__":
    main()
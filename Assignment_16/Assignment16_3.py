# Write a program which contains one function named as add() hich accepts wo numbers from user and return addition of that numbers

def Add():
    No1 = int(input("Enter No1 : "))
    No2 = int(input("Enter No2 : "))
    Ans = No1 + No2 
    print(Ans)

def main():
    Add()

if __name__=="__main__":
    main()
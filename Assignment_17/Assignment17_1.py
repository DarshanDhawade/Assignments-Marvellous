# Create on module named as arithimetic which contains 4 functions as Add() for addition Sub() for subtraction Mult() for multiplication
# Div() for division . All functions accepts two parameters as number and perform the operation
# Write on python program which call all the functions from arithmetic module by accepting the parameters from user
 
def Add(No1,No2):
    Result = No1 + No2
    print(Result)

def Sub(No1,No2):
    Result = No1 - No2
    print(Result)

def Mult(No1,No2):
    Result = No1 * No2
    print(Result)

def Div(No1,No2):
    Result = No1 / No2
    print(Result)


def main():
    No1=int(input("Enter No1 : "))
    No2=int(input("Enter No2 : "))
    Add(No1,No2)
    Sub(No1,No2)
    Mult(No1,No2)
    Div(No1,No2)

if __name__=="__main__":
    main()
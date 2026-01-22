# Write a program which accepts one number and prints all odd numbers till that number
def Odd():
    No = int(input("Enter Number : ")) 
    i = 1

    for i in range(1,No+1,2):
        print(i)
        
def main():
    Odd()

if __name__=="__main__":
    main()
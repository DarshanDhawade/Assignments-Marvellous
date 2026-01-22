# Write a program which accepts one number and prints factorial of that number
def Factorial():
    No = int(input("Enter number : "))
    i = 1

    for i in range(1,No):
        No = No * i
        print(No)

def main():
    Factorial()

if __name__ == "__main__":
    main()
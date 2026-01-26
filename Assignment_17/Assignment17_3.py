# Write a program which accept one number and returns its factorial

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
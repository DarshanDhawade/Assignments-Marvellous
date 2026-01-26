# Write a program which accept one number and display the below pattern

def main():
    No = int(input("Enter size : "))

    for x in range(No):
        for y in range(1,No+1):
            print(y ,end=" ")
        print()

if __name__=="__main__":
    main()
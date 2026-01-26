# Write a program which accept one number and display the below pattern

def main():
    No = int(input("Enter size : "))
    for x in range(No,0,-1):
        print("*" * x)
        
if __name__=="__main__":
    main()
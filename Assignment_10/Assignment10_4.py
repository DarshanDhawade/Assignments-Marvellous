# Write a program which accepts one number and prints all even numbers till that number
def Even():

    No = int(input("Enter Number : ")) #10
    i = 1

    for i in range(0,No+1,2):
        print(i)
        
def main():
    Even()

if __name__=="__main__":
    main()
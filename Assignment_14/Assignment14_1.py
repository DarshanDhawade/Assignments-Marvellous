# Write a lambda function which accepts one number and returns square of that number.

x = int(input("Enter Number : "))

def main():
    square = lambda x : x * x
    print(square(x)) #25

if __name__=="__main__":
    main()
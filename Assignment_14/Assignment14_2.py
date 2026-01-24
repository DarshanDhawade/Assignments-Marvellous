# Write a a lambda function which accepts one number and return cube of that number

x = int(input("Enter Number : "))

def main():

    cube = lambda x : x ** 3
    print(cube(x)) 

if __name__=="__main__":
    main()
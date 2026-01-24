# Write a lambda function which accepts two numbers and returns true if number is even otherswise false

def main():
    IsEven = lambda No : True if No % 2 == 0 else False
    print(IsEven(50))

if __name__=="__main__":
    main()
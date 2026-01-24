# Write a lambda function which accepts two numbers and returns true if number is odd otherswise false

def main():
    IsOdd = lambda No : True if No % 2 == 1 else False
    print(IsOdd(50))

if __name__=="__main__":
    main()
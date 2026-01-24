# Write a lambda function which accepts one number and returns true if divisible by 5

def main():
    Divisible5 = lambda No : True if No % 5 == 0 else False
    print(Divisible5(50))

if __name__=="__main__":
    main()
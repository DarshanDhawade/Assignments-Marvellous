# Write a lambda function which accepts three numbers and returns largest number

def main():
    Largest = lambda No1,No2,No3 : max(No1,No2,No3)
    print(Largest(11,10,21))

if __name__=="__main__":
    main()
# Write a lambda function using filter () which accepts a list of number and returns a list of odd numbers

def main():
    Numbers = [1,2,3,4,5,6,7,8,9,10]

    CheckOdd = list(filter(lambda Numbers : Numbers % 2 == 1,Numbers))
    print(CheckOdd)

if __name__=="__main__":
    main()
# Write a lambda function using map() which accepts list of numbers and returns a list of squares of each number 

def main():
    Numbers = [3,4,5,6,7]

    Square = list(map(lambda Numbers : Numbers ** 2,Numbers))
    print(Square)

if __name__=="__main__":
    main()
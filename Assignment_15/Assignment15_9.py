# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce

def main():
    Numbers = [1,3,10,0,34,1000,89]

    Product = reduce(lambda x,y: x * y ,Numbers)
    print(Product)

if __name__=="__main__":
    main()
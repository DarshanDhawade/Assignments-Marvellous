# Write a lambda function using reduce () which accepts a list of number and returns a addition of that numbers

from functools import reduce

def main():
    Numbers = [1,2,3,4,5,6,7,8,9,10]

    Sum = reduce(lambda x,y: x + y ,Numbers)
    print(Sum)

if __name__=="__main__":
    main()
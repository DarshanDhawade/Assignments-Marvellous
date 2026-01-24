# Write a lambda function using reduce () which accepts a list of number and returns minimum element

from functools import reduce

def main():
    Numbers = [10,1000,100,10000,1]

    MinElement= reduce(lambda x,y: x if x < y else y ,Numbers)
    print(MinElement)

if __name__=="__main__":
    main()
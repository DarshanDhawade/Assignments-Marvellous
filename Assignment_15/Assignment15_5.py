# Write a lambda function using reduce () which accepts a list of number and returns maximum element

from functools import reduce

def main():
    Numbers = [10,1000,100,10000,1]

    MaxElement= reduce(lambda x,y: x if x > y else y ,Numbers)
    print(MaxElement)

if __name__=="__main__":
    main()
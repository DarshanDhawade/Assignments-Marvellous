# Write a program which contains filter), map() and reduce) in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even
# Map function will calculate square . Reduce will return addition of all that number 

from functools import reduce

def main():
    numbers = list(map(int,input("Enter numbers ").split( )))

    filtered = list(filter(lambda x : x % 2 == 0, numbers))

    mapped = list(map(lambda x : x ** 2 , filtered))

    if mapped :
        product = reduce (lambda x,y :x + y , mapped )
    else :
        product = 0 

    print("After Filter  : " , filtered)
    print("After Map : " , mapped )
    print("After Reduce : ", product)
    

if __name__ == "__main__":
    main()

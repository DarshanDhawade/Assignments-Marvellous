# Write a program which contains filter), map() and reduce) in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that number 

from functools import reduce

def main():
    numbers = list(map(int,input("Enter numbers ").split( )))

    filtered = list(filter(lambda x : x > 70 and x <= 90 , numbers))

    mapped = list(map(lambda x : x + 10 , filtered))

    if mapped :
        product = reduce (lambda x,y :x * y , mapped )
    else :
        product = 0 

    print("After Filter  : " , filtered)
    print("After Map : " , mapped )
    print("After Reduce : ", product)
    

if __name__ == "__main__":
    main()

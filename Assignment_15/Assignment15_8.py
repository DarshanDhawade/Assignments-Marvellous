# Write a lambda function using filter () which accepts a list of numbers and returns and returns the list of numbers divisible by 3 and 5

def main():
    Numbers= [10,15,30,45,90,7,12]
    DivisibleBY_5= list(filter(lambda x:  x % 3 == 0 and x % 5 == 0  ,Numbers))
    print(DivisibleBY_5)

if __name__=="__main__":
    main()
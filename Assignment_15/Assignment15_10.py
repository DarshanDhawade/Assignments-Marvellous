# Write a lambda function using filter () which accepts a list of numbers and returns and returns the count of even numbers

def main():
    Numbers= [10,15,30,45,90,7,12]
    CountEven= len(list(filter(lambda x: x % 2 == 0 ,Numbers)))
    print(CountEven)

if __name__=="__main__":
    main()
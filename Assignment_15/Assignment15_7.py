# Write a lambda function using filter () which accepts a list of strings and returns and returns the list of strings having len greater than 5


def main():
    Words = ["Elephant","Maths","Egg","Hundred","Assignment"]
    StringOf5= list(filter(lambda x: len(x) > 5  ,Words))
    print(StringOf5)

if __name__=="__main__":
    main()
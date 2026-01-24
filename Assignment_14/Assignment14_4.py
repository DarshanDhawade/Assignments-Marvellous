# Write a lambda function which accepts two numbers and returns minimum number
def main():
    MinNum = lambda No1,No2 : No1 if No1<No2 else No2
    print(MinNum(10,12))

if __name__=="__main__":
    main()

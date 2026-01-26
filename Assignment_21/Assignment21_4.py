# Design a python application that creates two threads named sum of elements and product of element

import threading

def Sum(Numbers):
    Addition = Numbers[0]
    for i in Numbers:
            Addition = Addition + i
    print("Sum of Numbers: ",Addition)

def Product(Numbers):
    Multiplication = Numbers[0]
    for i in Numbers:
            Multiplication = Multiplication * i
    print("product of numbers : ",Multiplication)

def main():

    No = int(input("Enter Count : "))
    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)
    print(Numbers)

    t1 = threading.Thread(target=Sum,args= (Numbers,))
    t2 = threading.Thread(target=Product, args=(Numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
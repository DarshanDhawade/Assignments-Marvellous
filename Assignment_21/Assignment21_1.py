# Design a python application that creates two threads named prime and non prime

import threading

def ChkPrime(No):
    if No <= 1:
        return False 
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def Prime(data):
    print("Prime Numbers are : ")
    for i in data:
        if ChkPrime(i):
            print(i)

def NonPrime(data):
    print(" Non Prime Numbers are : ")
    for i in data:
        if not ChkPrime(i):
            print(i)

def main():

    No = int(input("Enter Count : "))
    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)
    print(Numbers)

    t1 = threading.Thread(target=Prime,args= (Numbers,))
    t2 = threading.Thread(target=NonPrime, args=(Numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
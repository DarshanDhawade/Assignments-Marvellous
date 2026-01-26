# Design a python application that creates two seperate threads named EvenFactor and Oddfactor

import threading

def EvenFactor(No):
    even_sum = 0
    print("Inside even factor ")
    
    for i in range(1,No + 1):
        if No % i == 0 and i % 2 == 0: 
            print(i)
            even_sum += i

    print("Sum of even factors : ",even_sum)
    print("even thread finish")


def OddFactor(No):
    print("Inside odd factor ")
    odd_sum = 0
    for i in range(1,No + 1):
        if No % i == 0 and i % 2 == 1: 
            print(i)
            odd_sum += i

    print("Sum of odd factors : ",odd_sum)
    print("odd thread finish")

def main():

    No = int(input("Enter Number : "))
    t1 = threading.Thread(target=EvenFactor,args= (No,), name="EvenFactor Thread")
    t2 = threading.Thread(target=OddFactor, args=(No,),name="OddFactor Thread")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
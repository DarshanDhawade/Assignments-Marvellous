# Design a python application that creates two seperate threads named EvenList and OddList

import threading

def EvenList(No):
    even_list = []
    even_sum = 0
    print("Inside even factor ")
    
    for i in No:
        if i % 2 == 0: 
            even_list.append(No)
            print(i)
            even_sum += i
    
    print("Even Numbers : ",even_list)
    print("Sum of even numbers : ", even_sum)
    print("even thread finish")


def OddList(No):
    print("Inside odd factor ")
    odd_list = []
    odd_sum = 0

    for i in No: 
        if i % 2 == 1: 
            odd_list.append(No)
            print(i)
            odd_sum += i

    print("Odd numbers : ",odd_list)
    print("Sum of odd numbers : ", odd_sum)
    print("odd thread finish")

def main():

    No = list(map(int,input("Enter Numbers using space : ").split( )))
    t1 = threading.Thread(target=EvenList,args= (No,))
    t2 = threading.Thread(target=OddList, args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
# Design a python application that creates two threads named maximum element and minimum element

import threading

def Max(Numbers):
    Max_value = Numbers[0]
    for i in Numbers:
        if i > Max_value:
            Max_value = i
    print("Maximum Number is : ",Max_value)

def Min(Numbers):
    Min_value = Numbers[0]
    for i in Numbers:
        if i > Min_value:
            Min_value = i
    print("Maximum Number is : ",Min_value)

def main():

    No = int(input("Enter Count : "))
    Numbers = []

    for i in range(No):
        num = int(input("Enter number : "))
        Numbers.append(num)
    print(Numbers)

    t1 = threading.Thread(target=Max,args= (Numbers,))
    t2 = threading.Thread(target=Min, args=(Numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
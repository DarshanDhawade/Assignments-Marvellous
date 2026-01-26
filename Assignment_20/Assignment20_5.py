# Design a python application that creates two seperate threads named thread1 and thread 2 1 to 50 and 50 to 1

import threading

def No1_50():
    print("Inside 1 to 50 ")
    for i in range(1,51):
        print(i)

    print("1 to 50 Thread1 Finish ")

def No50_1():
    print("Inside Reverse ")
    for i in range(50,0,-1):
        print(i)

    print("Reverse Thread2 Finish ")

def main():
    t1 = threading.Thread(target=No1_50, name="Thread1")
    t2 = threading.Thread(target=No50_1, name="Thread2")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("main finsihed")

if __name__=="__main__":
    main()
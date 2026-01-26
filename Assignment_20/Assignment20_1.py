# Design a python application that creates two seperate threads named even and odd

import threading

def EvenNo():
    print("Inside even ")
    for i in range(2,21,2):
        print(i)

    print("Even Thread Finish ")

def OddNo():
    print("Inside odd ")
    for i in range(1,20,2):
        print(i)

    print("Odd Thread Finish ")

def main():
    t1 = threading.Thread(target=EvenNo, name="even")
    t2 = threading.Thread(target=OddNo, name="odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main finsihed")

if __name__=="__main__":
    main()
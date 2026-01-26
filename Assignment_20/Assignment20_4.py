# Design a python application that create 3 threads named small capital and digits
import threading

def count_small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1

    print("Thread Id : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)
    print("small characters : ",count)
    print()

def count_capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1

    print("Thread Id : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)
    print("Capital characters : ",count)
    print()

def count_digit(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1

    print("Thread Id : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)
    print("digit characters : ",count)
    print()


def main():
    str_input = input("Enter a string : ")

    t1 = threading.Thread(target=count_small,args=(str_input,) ,name="Small")
    t2 = threading.Thread(target=count_capital,args=(str_input,), name="Capital")
    t3 = threading.Thread(target=count_digit,args=(str_input,),name="Digits")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("main finsihed")

if __name__=="__main__":
    main()
#Design a python application where multiple threads update a shared variable

import threading

iCnt = 0 
lobj = threading.Lock() 

def update():
    global iCnt

    for _ in range(2000000):
        with lobj:
            iCnt = iCnt + 1


def main():
    global iCnt

    t1 = threading.Thread(target = update)
    t2 = threading.Thread(target = update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("value of iCnt is : " , iCnt)

if __name__=="__main__":
    main()
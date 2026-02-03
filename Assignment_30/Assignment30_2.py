# Write a program which accepts a file name from the user and counts total number of words 

import sys 

def FileScanner(FileName):
    f = open(FileName,"r")
    Data = f.read()
    words = Data.split()
    print(len(words))


def main():
    if (len(sys.argv) !=2):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileScanner(sys.argv[1])

if __name__=="__main__":
    main()
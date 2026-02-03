# Write a program which accepts a file name from the user and counts how many lines are present in the file

import sys 

def FileScanner(FileName):
    f = open(FileName,"r")
    Data = f.readlines()
    print(len(Data))


def main():
    if (len(sys.argv) !=2):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileScanner(sys.argv[1])

if __name__=="__main__":
    main()
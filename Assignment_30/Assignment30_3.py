# Write a program which accepts a file name from the user and display the contents line by line

import sys 

def FileScanner(FileName):
    f = open(FileName,"r")
    Data = f.read()
    print(Data)

def main():
    if (len(sys.argv) !=2):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileScanner(sys.argv[1])

if __name__=="__main__":
    main()
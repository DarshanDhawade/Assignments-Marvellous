# Write a python program which accepts a file name from user and checks whether that file exists in the current directory or not

import os

def FileScanner(FileName):

    ret = os.path.exists(FileName)

    if(ret == False):
        print("There is no such file")
        return
    else:
        print("There is a file name : ",FileName)
    
def main():
    FileName = input("Enter the name of directory : ")
    FileScanner(FileName)

if __name__=="__main__":
    main()
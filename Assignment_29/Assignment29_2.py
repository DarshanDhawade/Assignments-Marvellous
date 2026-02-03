# Write a python program which accepts a file name from user opens that file and display the entire content 

import os

def FileScanner(FileName):

    ret = os.path.exists(FileName)

    if (ret == True):
        print("Yes there is a file")
        f = open(FileName,"r")

        Data = f.read()

        print("Contents of the file are : ",Data)

    else:
        print("There is no such file")
        return
    
def main():
    FileName = input("Enter the name of directory : ")
    FileScanner(FileName)

if __name__=="__main__":
    main()
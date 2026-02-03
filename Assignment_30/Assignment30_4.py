# Write a program which accepts 2 file name from the user and copy all contents from one to second

import sys

def FileScanner(FileName1,FileName2):

    with open(FileName1,"r") as copyfile:
        Data = copyfile.read()

    print("Existing File is opened")

    with open(FileName2,"w") as pastefile:
        pastefile.write(Data)

    print("New File is created and pasted")
    
def main():
    if (len(sys.argv) !=3):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileScanner(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()
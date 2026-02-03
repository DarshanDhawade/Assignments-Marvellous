# Write a program which accepts an existing file name through command line argument, creates new file named demo.txt and copies all contents from he given file into demo.txt

import sys

def FileScanner(FileName):

    with open(FileName,"r") as copyfile:
        Data = copyfile.read()

    print("Existing File is opened")

    with open("Demo.txt","w") as pastefile:
        pastefile.write(Data)

    print(" New File is created and pasted")
    
def main():
    if (len(sys.argv) !=2):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileScanner(sys.argv[1])

if __name__=="__main__":
    main()
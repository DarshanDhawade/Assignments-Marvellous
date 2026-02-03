# Write a program which accepts an existing file name through command line argument and compares the content of both files
import sys

def FileScanner(FileName1,FileName2):
    with open(FileName1,"r") as file1 , open(FileName2,"r") as file2:
        if file1.read() == file2.read():
            print("Success")
        else:
            print("Failure")
    
def main():
    if (len(sys.argv) !=3):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileScanner(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()
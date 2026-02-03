# Write a program which accepts a file name and a word from the user and checks whether the word is present or not
import sys

def FileScanner(FileName,word):
    f = open(FileName,"r")
    Data = f.read()
    if word in Data:
        print("The word is present")
    else:
        print("The word is not present")
    
def main():
    if (len(sys.argv) !=3):
        print("invalid number of arguments")
        print("please specify the name of file")
        return
    
    FileName = sys.argv[1]
    word = sys.argv[2]
    FileScanner(FileName,word)
    
if __name__=="__main__":
    main()

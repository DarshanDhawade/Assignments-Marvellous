# Returns the frequency count of string

import sys

def FileScanner(FileName,word):
    count = 0
    with open(FileName,"r") as file :
        for line in file:
            datas = line.lower().split()
            for data in datas:
               if data == word.lower():
                   count += 1
    print(f"Frequency of '{word}' is : ",count)

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
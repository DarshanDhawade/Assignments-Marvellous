# Design an automation script which accept directory name and write names of duplicate files from that directory 
# into a log file named as log.txt log.txt should be created in the current directory


import os
import sys
import hashlib

def Calculate_Hash(filename):
    hobj = hashlib.md5()

    with open(filename,"rb") as f:
        while True:
            buffer = f.read(1024)
            if not buffer:
                break
            hobj.update(buffer)

    return hobj.hexdigest()

def Find_Duplicate(DirName):
    hash_dict = {}
    duplicate = []

    for foldername,subfolders,filenames in os.walk(DirName):
        for file in filenames:
            filepath = os.path.join(foldername,file)
            print("Checking file:", filepath)

            try:
                file_hash = Calculate_Hash(filepath)

                if file_hash in hash_dict:
                    duplicate.append
                else:
                    hash_dict[file_hash] = filepath
            
            except Exception:
                continue

    return duplicate

def main():
    if (len(sys.argv) !=2):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    DirName = sys.argv[1]

    duplicate = Find_Duplicate(DirName)

    with open("log.txt", "w") as log_file:
        for file in duplicate:
            log_file.write(file + "\n")

    print("Duplicate file names written to log.txt")

if __name__=="__main__":
    main()

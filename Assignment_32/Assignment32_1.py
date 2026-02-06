# Design an automation script which accept directory name and display checksum of all files
import os
import sys
import hashlib


def CalculateChecksum(FileName):
        fobj = open(FileName,"rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1000)

        while(len(Buffer)>0):
            hobj.update(Buffer)
        Buffer = fobj.read(1000)

        fobj.close()

        return hobj.hexdigest()


def DirectoryWatcher(DirName):
    ret = False
    ret = os.path.exists(DirName)

    if ret == False:
        print("there is no such directory")
        return
    
    ret = os.path.isdir(DirName)

    if ret == False:
        print("it is not a directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            print(f"File Name : {fname} Checksum : {Checksum} ")

def main():
    if (len(sys.argv) !=2):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    DirectoryWatcher(sys.argv[1])

if __name__=="__main__":
    main()

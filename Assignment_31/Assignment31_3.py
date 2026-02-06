# Design Automation Script which accept two directory names and copy all files from first directory into second directory as temp and copy all files from demo to temp

import shutil
import os
import sys

def DirectoryCopy(OldDirName,NewDirName):

    if not os.path.isdir(OldDirName):
        print("Wrong Directory Path")
        return
    
    if not os.path.isdir(NewDirName):
        print("Wrong Directory Path")
        return
    
    for filename in os.listdir(OldDirName):
        old_file = os.path.join(OldDirName,filename)
        new_file = os.path.join(NewDirName,filename)

        if os.path.isfile(old_file):
            shutil.copy(old_file,new_file)
    
    print("files copied ")
   
    
def main():
    if (len(sys.argv) !=3):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()

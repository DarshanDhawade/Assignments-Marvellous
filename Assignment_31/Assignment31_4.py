# Design Automation Script which accept two directory names and one extension and copy all files of that extension to the 2nd directory

import shutil
import os
import sys

def DirectoryCopy(OldDirName,NewDirName,Extension):

    if not os.path.isdir(OldDirName):
        print("Wrong Directory Path")
        return
    
    if not os.path.isdir(NewDirName):
        print("Wrong Directory Path")
        return
    
    
    for filename in os.listdir(OldDirName):
        if filename.endswith(Extension):
            old_file = os.path.join(OldDirName,filename)
            new_file = os.path.join(NewDirName,filename)

            if os.path.isfile(old_file):
                shutil.copy(old_file,new_file)
    
    print("files copied ")
   
    
def main():
    if (len(sys.argv) !=4):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    DirectoryCopy(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__=="__main__":
    main()

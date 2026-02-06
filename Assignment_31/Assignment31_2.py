# Design Automation Script which accept directory name and two file extension from user. Rename all the file with first extension with the second

import os
import sys

def RenameExt(DirName,OldExtension,NewExtension):

    if not os.path.isdir(DirName):
        print("Wrong Directory Path")
        return
    
    if not OldExtension.startswith("."):
        OldExtension = "." + OldExtension

    if not NewExtension.startswith("."):
        NewExtension = "." + OldExtension

    Renamed= False

    for file in os.listdir(DirName):
        if file.endswith(OldExtension):
            old_path = os.path.join(DirName,file)
            new_name = file[:-len(OldExtension)] + NewExtension
            new_path = os.path.join(DirName,new_name)
            os.rename(old_path,new_path)
            print(f"Renamed {file} -> {new_name}")
            Renamed = True

    if not Renamed:
        print("No files with extension")

def main():
    if (len(sys.argv) !=4):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    RenameExt(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__=="__main__":
    main()

# Design Automation Script which accept directory name and file extension from user. Display all files with that extension
import os
import sys

def DirectoryScanner(DirName,Extension):

    if not os.path.isdir(DirName):
        print("Wrong Directory Path")
        return
    if not Extension.startswith("."):
        Extension = "." + Extension

    print(f"\nFiles with '{Extension}' Extension in '{DirName}':\n")
    found = False

    for file in os.listdir(DirName):
        if file.endswith(Extension):
            print(file)
            found = True

    if not found:
        print("No files with extension")

def main():
    if (len(sys.argv) !=3):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()

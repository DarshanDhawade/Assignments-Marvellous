# Design an automation script which accept directory name and write names of duplicate files from that directory 
# into a log file named as log.txt log.txt should be created in the current directory
# remove the duplicates 
# add time

import os
import sys
import hashlib
import time

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
    deleted_files = []

    for foldername,subfolders,filenames in os.walk(DirName):
        for file in filenames:
            filepath = os.path.join(foldername,file)
            print("Checking file:", filepath)

            try:
                file_hash = Calculate_Hash(filepath)

                if file_hash in hash_dict:
                    os.remove(filepath)
                    deleted_files.append(filepath)
                else:
                    hash_dict[file_hash] = filepath
            
            except Exception:
                continue

    return deleted_files

def main():
    if (len(sys.argv) !=2):
        
        print("invalid number of arguments")
        print("please specify the name of directory")
        return

    DirName = sys.argv[1]

    start_time = time.time()

    deleted_files = Find_Duplicate(DirName)

    end_time = time.time()
    total_time = end_time - start_time

    with open("log.txt", "w") as log_file:
        log_file.write("Duplicate File Removal Log\n")
        log_file.write("=================================\n")
        log_file.write(f"Start Time: {time.ctime(start_time)}\n")
        log_file.write(f"End Time: {time.ctime(end_time)}\n")
        log_file.write(f"Execution Time: {total_time:.4f} seconds\n\n")

        if deleted_files:
            log_file.write("Deleted Files:\n")
            for file in deleted_files:
                log_file.write(file + "\n")
        else:
            log_file.write("No duplicate files found\n")
        print("Duplicate file names written to log.txt")

if __name__=="__main__":
    main()

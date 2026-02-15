import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import logging
import smtplib
from email.message import EmailMessage

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    zip_name = folder + "_" +timestamp + ".zip"

    # open the zip file
    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()

    return zip_name

def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_files = []

    print("Createing the Bckup folder for backup process")

    os.makedirs(Destination, exist_ok= True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            if file.endswith((".tmp", ".log", ".exe")):
                continue
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok= True)
    
            # Copy the files if its new
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files

    
def MarvellousDataShieldStart(Source = "Data"):
    Border = "-"*50
    
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Process Started succesfully at : ",time.ctime())
    print(Border)

    logging.info("Backup started")


    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    logging.info(f"Files copied: {len(files)}")
    logging.info(f"Zip created: {zip_file}")
    logging.info("Backup completed successfully")

    print(Border)
    print("Backup completed succesfully")
    print("Files copied : ",len(files))
    print("Zip file gets creatd : ",zip_file)
    print(Border)

    with open("BackupHistory.txt", "a") as history:
        history.write(f"{time.ctime()} | Files: {len(files)} | Zip: {zip_file}\n")

    SendEmail(zip_file, len(files))


def SetupLogger():
    logging.basicConfig(
        filename="MarvellousBackup.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def SendEmail(zip_file, file_count):

    sender_email = "testingd2003@gmail.com"
    sender_password = "bfup uvsp tgcj sgta"
    receiver_email = "darshandhawade9@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Marvellous Data Shield Backup Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    body = f"""
Backup Completed Successfully

Files Copied: {file_count}
Zip File: {zip_file}
Time: {time.ctime()}
"""

    msg.set_content(body)

    with open(zip_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename=zip_file
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully")

def RestoreBackup(zip_name, destination):

    print("Restoring backup...")

    with zipfile.ZipFile(zip_name, 'r') as z:
        z.extractall(destination)

    print("Restore completed successfully")



def main():

    SetupLogger()

    Border = "-" * 50

    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    # -------------------------------
    # CASE 1 : HELP / HISTORY
    # -------------------------------
    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("This script is used to:")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create archive of backup")
            print("4 : Send email notification")
            print("5 : Restore backup")
            print("6 : Show backup history")

        elif sys.argv[1] == "--history":
            if os.path.exists("BackupHistory.txt"):
                with open("BackupHistory.txt", "r") as f:
                    print(f.read())
            else:
                print("No backup history found.")

        else:
            print("Invalid option")

    # -------------------------------
    # CASE 2 : RESTORE
    # -------------------------------
    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        RestoreBackup(sys.argv[2], sys.argv[3])

    # -------------------------------
    # CASE 3 : SCHEDULER BACKUP
    # -------------------------------
    elif len(sys.argv) == 3:

        interval = int(sys.argv[1])
        source_folder = sys.argv[2]

        schedule.every(interval).minutes.do(
            MarvellousDataShieldStart, source_folder
        )

        print(Border)
        print("Data Shield System started successfully")
        print("Time interval (minutes):", interval)
        print("Press Ctrl + C to stop")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
    
if __name__ == "__main__":
    main()
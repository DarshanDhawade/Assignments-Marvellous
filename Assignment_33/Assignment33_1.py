import psutil
import sys
import os
import time 
import schedule
import threading
import smtplib
from email.message import EmailMessage


def CreateLog(FolderName):
    Border = "_"*50

    Ret = os.path.exists(FolderName)

    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        if (Ret == False):
            print("Unable to create Folder")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory For Log File is created")

    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timestamp)

    with open(FileName,"w") as fobj:

        fobj.write(Border+"\n")

        fobj.write("__________Marvellous Platform Survelliance System__________\n")
        fobj.write("Log Created at time :"+ time.ctime()+"\n")
        fobj.write(Border+"\n")

        #CPU USAGE
        fobj.write("CPU Usage : %s %% \n" %psutil.cpu_percent())
        
        #RAM USAGE
        mem = psutil.virtual_memory()
        fobj.write("RAM Usage : %s %% \n " %mem.percent)

        # DISK USAGE REPORT

        for part in psutil.disk_partitions():
            try :
                usage = psutil.disk_usage(part.mountpoint)
                fobj.write("%s -> %s %% used\n" %(part.mountpoint,usage.percent))
            except:
                pass

        # NETWORK USAGE REPORT 

        net = psutil.net_io_counters()
        fobj.write("sent : %.2f MB\n" %(net.bytes_sent / (1024*1024)))
        fobj.write("recv : %.2f MB\n" %(net.bytes_recv / (1024*1024)))

        # PROCESS LOGIN SECTION
        
        Data = ProcessScan()

        for info in Data:
            fobj.write("PID : %s\n" %info.get("pid"))
            fobj.write("Name : %s\n" %info.get("name"))
            fobj.write("Threads : %s\n" %info.get("num_threads"))
            fobj.write("CPU %% : %s\n" %info.get("cpu_percent"))
            fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
            fobj.write("RSS (MB) : %.2f\n" %info.get("rss"))
            fobj.write("VMS (MB) : %.2f\n" %info.get("vms"))
            fobj.write("Open Files : %s\n" %info.get("open_files"))
            fobj.write("_"*50 + "\n")

        fobj.write("\nTop 10 Memory Consuming Processes\n")
        fobj.write("_"*50 + "\n")

        for info in Data[:10]:
            fobj.write("%s -> %.2f %%\n" %(info.get("name"),info.get("memory_percent")))

        SendEmail(FileName, Data)
            

def ProcessScan():
    
    ProcessData = []

    # Warm up CPU calculation
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status","create_time"])

            # Format time
            info["create_time"] = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(info["create_time"]))

            # CPU and Memory %
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            # Thread count
            info["num_threads"] = proc.num_threads()

            # RSS and VMS
            mem_info = proc.memory_info()
            info["rss"] = mem_info.rss / (1024 * 1024)
            info["vms"] = mem_info.vms / (1024 * 1024)

            # Open files
            try:
                info["open_files"] = len(proc.open_files())
            except:
                info["open_files"] = "Access Denied"

            ProcessData.append(info)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    # Sort by memory %
    ProcessData = sorted(ProcessData,key=lambda x: x.get("memory_percent", 0),reverse=True)

    return ProcessData

def SendEmail(logfile, process_data):

    sender_email = "testingd2003@gmail.com"
    sender_password = "bfup uvsp tgcj sgta"
    receiver_email = "darshandhawade9@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Platform Surveillance Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # ---------- SUMMARY SECTION ----------
    total_processes = len(process_data)

    top_cpu = sorted(process_data,
                     key=lambda x: x.get("cpu_percent", 0),
                     reverse=True)[:5]

    top_memory = process_data[:5]

    top_threads = sorted(process_data,
                         key=lambda x: x.get("num_threads", 0),
                         reverse=True)[:5]

    top_open = sorted(process_data,
                      key=lambda x: x.get("open_files")
                      if isinstance(x.get("open_files"), int) else 0,
                      reverse=True)[:5]

    body = f"""
Platform Surveillance System Report

Total Processes: {total_processes}

Top 5 CPU Processes:
{[(p["name"], p["cpu_percent"]) for p in top_cpu]}

Top 5 Memory Processes:
{[(p["name"], p["memory_percent"]) for p in top_memory]}

Top 5 Thread Count Processes:
{[(p["name"], p["num_threads"]) for p in top_threads]}

Top 5 Open File Processes:
{[(p["name"], p["open_files"]) for p in top_open]}
"""

    msg.set_content(body)

    # ---------- ATTACH LOG FILE ----------
    with open(logfile, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(logfile)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    # ---------- SEND EMAIL ----------
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully")

def SchedulerThread(interval, directory):

    schedule.every(interval).minutes.do(CreateLog, directory)

    print("Platform Surveillance System Started")
    print("Press Ctrl + C to stop")

    while True:
        schedule.run_pending()
        time.sleep(1)

        
def main():

    print("__________Marvellous Platform Survelliance System__________")

    if (len(sys.argv) == 2):
        if(sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("this script is used to : ")
            print("1 : create automatic logs")
            print("2 : executes periodically")
            print("3 : sends mail with log")
            print("4 : stores information abouty processes")
            print("5 : store information about CPU")
            print("6 : store information about RAM")
            print("7 : store information about secondary storage")

        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("use the automation script as ")
            print("scriptname.py timeinterval directoryname")
            print("time interval : the time in munutes for periodic schedule")
            print("directory name : name of dirctory to create auto logs")

        else:
            print("unable to proceed as there is no such option")
            print("please use --h or --u to get more details")

    # python3 Demo.py 5 Marvellous
    elif(len(sys.argv)==3):

        interval = int(sys.argv[1])
        directory = sys.argv[2]

        t1 = threading.Thread(target=SchedulerThread,args=(interval, directory),daemon=True)    
        t1.start()

        while True:
            time.sleep(1)
    else:
        print("invalid number of command line arguments")
        print("unable to proceed as there is no such option")
        print("please use --h or --u to get more details")  

if __name__=="__main__":
    main()
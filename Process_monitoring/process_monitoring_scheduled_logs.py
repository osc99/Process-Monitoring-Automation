import schedule
from sys import *
import time
import smtplib
import psutil
import os

def ProcessLog(log_dir="ABC"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir) #if directory not present create new
        except:
            pass  # is same as continue

    separator = "-" * 80
    log_path = os.path.join(log_dir, " file %s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Process Logger:""\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Log file is successfully generated at location %s" % (log_path))


def main():
    print("Process Monitoring Automation....")
    print("Application name:" + argv[0])
    print(argv[1])
    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")    


if __name__ == "__main__":
    main()

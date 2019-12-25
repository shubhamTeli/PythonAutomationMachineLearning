"""
Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLogFileInDir.py Demo
Demo is name of Directory.

"""
import sys
import time;
import psutil;
import os;

def processLogger(dirName):

    if not os.path.exists(dirName):
        os.mkdir(dirName);

    listProcess=[];
    logfile="RunningProcesses.log";
    log_path=os.path.join(dirName,logfile)
    with open(log_path,'w') as fobj:
        separator="-"*80;
        fobj.write(separator + "\nProcess Logger : " + str(time.ctime()) + "\n" + separator + "\n" );

        for pro in psutil.process_iter():
            try:
                pinfo=pro.as_dict(attrs=['pid','name','username']);
                listProcess.append(pinfo);
            except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                pass;
        for element in listProcess:
            fobj.write("%s\n"%element);

def main():
      try:
         processLogger(str(sys.argv[1]));

      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
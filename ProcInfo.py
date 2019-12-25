"""
Design automation script which display information of running processes as its name, PID,
Username.
"""
import time;
import psutil;


def processLogger():
    listProcess=[];
    logfile="RunningProcesses.log";
    with open(logfile,'w') as fobj:
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
         processLogger();

      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
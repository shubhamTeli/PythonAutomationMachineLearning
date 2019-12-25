"""
Design automation script which accept process name and display information of that process if
it is running.
Usage : SpecificProcInfo.py Notepad
"""
import sys
import time;
import psutil;

def isRunningProc(procName):

    listProcess = [];
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'username', 'name', 'cpu_times', 'create_time','memory_percent', 'memory_info'])
            if procName.lower() in pinfo['name'].lower():
                listProcess.append(pinfo)
                return listProcess;

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def processLogger(procName):

    decide=isRunningProc(procName);
    if not decide:
        print(procName + " process is not running.");
    else:
         logfile= procName + "ProcInfo.log";
         with open(logfile,'w') as fobj:
                separator="-"*80;
                fobj.write(separator + "\n" +str(procName) + " Process info : " + str(time.ctime()) + "\n" + separator + "\n" );
                for element in decide:
                    fobj.write("%s\n"%element);
         print(procName + " process is running, please go to  " + logfile + "  file for info.");

def main():
      try:
         processLogger(str(sys.argv[1]));

      except Exception as E:
          print("Exception occured: ",E);

if __name__ == "__main__":
    main();
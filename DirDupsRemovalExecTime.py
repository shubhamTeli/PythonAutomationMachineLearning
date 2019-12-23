"""
Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory. Display execution time required for the
script.
"""


import sys;
import os;
import time
import Checksum;

def DelDups(dic,starttime):
    results = list(filter(lambda x : len(x) > 1 ,dic.values()));

    if len(results) > 0:
        print("Duplicate files found and deleted!!!!");
        with open("OutputDirDupsRemovalExecTime.log",'w') as fobj:
            fobj.write("Following Duplicate files are deleted successfully!!!!");
            fobj.write("\n" + "---" * 30);
            for result in results:
                fcnt=0;
                for subresult in result:
                    fcnt+=1;
                    if fcnt >= 2:
                        fobj.write("\n%s"%subresult);
                        os.remove(subresult);
            endtime=time.time();
            fobj.write("\n\n %s time took to execute."%(endtime-starttime));
        print("Output is stored in OutputDirDupsRemovalExecTime.log file");

    else:
        print("No duplicate files found to delete!!");


def findDups(path):

    flag=os.path.isabs(path);
    if flag == False:
        path=os.path.abspath(path);

    exists=os.path.exists(path);

    if exists:
        dupsfiles={};
        for dirName, subDir, files in os.walk(path):
            for fname in files:
                fname=os.path.join(dirName,fname);
                file_hash=Checksum.hashfile(fname);
                if file_hash in dupsfiles:
                        dupsfiles[file_hash].append(fname);
                else:
                    dupsfiles[file_hash]=[fname];
        return dupsfiles;
    else:
        print("Invalid path");


def main():
      try:
         starttime=time.time();
         dirName=sys.argv[1];
         arr=findDups(dirName);
         DelDups(arr,starttime);

      except Exception as E:
           print("Exception occured: ",E);


if __name__ == "__main__":
    main();
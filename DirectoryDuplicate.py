"""
Design automation script which accept directory name and write names of duplicate files from
that directory into log file named as Log.txt. Log.txt file should be created into current
directory.
"""


import sys;
import os;
import Checksum;

def printDups(dic):
    results = list(filter(lambda x : len(x) > 1 ,dic.values()));

    if len(results) > 0:
        print("Duplicate files found!!!!");
        with open("OutputDirDuplicateFiles.log",'w') as fobj:
            fobj.write("Duplicate files found!!!!");
            fobj.write("\n" + "---" * 30);
            for result in results:
                fcnt=0;
                for subresult in result:
                    fcnt+=1;
                    if fcnt >= 2:
                        fobj.write("\n%s"%subresult);
        print("Output is stored in OutputDirDuplicateFiles.log file");

    else:
        print("No duplicate files found!!");


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
         dirName=sys.argv[1];
         arr=findDups(dirName);
         printDups(arr);

      except Exception as E:
           print("Exception occured: ",E);


if __name__ == "__main__":
    main();
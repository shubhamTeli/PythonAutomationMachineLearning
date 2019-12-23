"""
Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory.
"""


import sys;
import os;
import Checksum;

def DelDups(dic):
    results = list(filter(lambda x : len(x) > 1 ,dic.values()));

    if len(results) > 0:
        print("Duplicate files found and deleted!!!!");
        with open("OutputDirDuplicateRemoval.log",'w') as fobj:
            fobj.write("Following Duplicate files are deleted successfully!!!!");
            fobj.write("\n" + "---" * 30);
            for result in results:
                fcnt=0;
                for subresult in result:
                    fcnt+=1;
                    if fcnt >= 2:
                        fobj.write("\n%s"%subresult);
                        os.remove(subresult);
        print("Output is stored in OutputDirDuplicateRemoval.log file");

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
         dirName=sys.argv[1];
         arr=findDups(dirName);
         DelDups(arr);

      except Exception as E:
           print("Exception occured: ",E);


if __name__ == "__main__":
    main();
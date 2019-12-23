#Design automation script which accept directory name and display checksum of all files.


import sys;
import os;
import Checksum;

def displayDirAllFileChecksum(path):

    flag=os.path.isabs(path);
    if flag == False:
        path=os.path.abspath(path);

    exists=os.path.exists(path);

    if exists:
        with open("OutputDirAllFileChecksum.log",'w') as fobj:
            for dirName, subDir, files in os.walk(path):
                for fname in files:
                    fobj.write("\n" + "-"*10);
                    fobj.write("\nFilename: "+ str(fname));
                    fname=os.path.join(dirName,fname);
                    fobj.write("\nChecksum: "+ str(Checksum.hashfile(fname)));

        print("Output is stored in OutputDirAllFileChecksum.log file");
    else:
        print("Invalid path");


def main():
      try:
         dirName=sys.argv[1];
         displayDirAllFileChecksum(dirName);

      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
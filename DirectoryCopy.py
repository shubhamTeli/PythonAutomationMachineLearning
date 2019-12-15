"""
Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
"""

import shutil;
import sys;
import os;

def dirCopy(sourceDir,targetDir):

    flag=os.path.isabs(sourceDir);
    if flag == False:
        sourceDir=os.path.abspath(sourceDir);

    exists=os.path.exists(sourceDir);

    if exists:
            os.mkdir(targetDir);
            for dirName, subDir, files in os.walk(sourceDir):
                cnt=0;
                for fname in files:
                    fname = os.path.join(dirName, fname);
                    shutil.copy(fname,targetDir);
                    cnt=+1;

            if cnt == 0:
                print("\nNo files found to copy.");
            else:
                print("files has been copied successfully!!!\n please go to directory and have a look.")

    else:
        print("Invalid path");


def main():
      try:
         dir1=sys.argv[1];
         dir2=sys.argv[2];
         dirCopy(dir1,dir2);

      except Exception as E:
          print("Exception occured: ",E)


if __name__ == "__main__":
    main();
"""
Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
"""

import shutil;
import sys;
import os;

def dirCopyExtn(sourceDir,targetDir,fExtn):

    flag=os.path.isabs(sourceDir);
    if flag == False:
        sourceDir=os.path.abspath(sourceDir);

    exists=os.path.exists(sourceDir);

    if exists:
            os.mkdir(targetDir);
            for dirName, subDir, files in os.walk(sourceDir):
                cnt=0;
                for fname in files:
                    if fname.endswith(fExtn):
                        fname = os.path.join(dirName, fname);
                        shutil.copy(fname,targetDir);
                        cnt=cnt+1;

            if cnt == 0:
                print("\nNo files found to copy.");
            else:
                print(str(cnt)+" files with "+str(fExtn)+" extension has been copied successfully!!!\n please go to directory and have a look.")

    else:
        print("Invalid path");


def main():
      try:
         dir1=sys.argv[1];
         dir2=sys.argv[2];
         fileExtn=sys.argv[3];
         dirCopyExtn(dir1,dir2,fileExtn);

      except Exception as E:
          print("Exception occured: ",E)


if __name__ == "__main__":
    main();
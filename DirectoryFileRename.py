#Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.


import sys;
import os;

def fileRename(path,sourceExtn,targetExtn):

    flag=os.path.isabs(path);
    if flag == False:
        path=os.path.abspath(path);

    exists=os.path.exists(path);

    if exists:
            for dirName, subDir, files in os.walk(path):
                cnt=0;
                for fname in files:
                    fname = os.path.join(dirName, fname);
                    pre,ext=os.path.splitext(fname);
                    if ext == sourceExtn:
                        os.rename(fname,pre + targetExtn);
                        cnt=+1;

            if cnt == 0:
                print("\nNo files have been renamed.");
            else:
                print("files has been renamed successfully!!!\n please go to directory and have a look.")

    else:
        print("Invalid path");


def main():
      try:
         dirName=sys.argv[1];
         fileExtn1=sys.argv[2];
         fileExtn2=sys.argv[3];
         fileRename(dirName,fileExtn1,fileExtn2);

      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
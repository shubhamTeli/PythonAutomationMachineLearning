#Design automation script which accept directory name and file extension from user. Display all files with that extension.


import sys;
import os;

def fileSearch(path,fExtn):

    flag=os.path.isabs(path);
    if flag == False:
        path=os.path.abspath(path);

    exists=os.path.exists(path);

    if exists:
        with open("OutputdirectoryFileSearchOutput.log",'w') as fobj:
            for dirName, subDir, files in os.walk(path):
                cnt=0;
                for fname in files:
                    if fname.endswith(fExtn):
                        if(cnt==0):
                            fobj.write("Below are the files with extension " + str(fExtn) +"\n");
                        fobj.write("\n" + str(fname));
                        cnt=+1;
            if cnt == 0:
                fobj.write("No files found with extension " + str(fExtn));
        print("Output is stored in OutputdirectoryFileSearchOutput.log file");
    else:
        print("Invalid path");


def main():
      try:
         dirName=sys.argv[1];
         fileExtn=sys.argv[2];
         fileSearch(dirName,fileExtn);

      except Exception as E:
          print("Exception occured: ",E);


if __name__ == "__main__":
    main();
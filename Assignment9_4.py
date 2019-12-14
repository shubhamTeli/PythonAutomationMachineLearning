"""
Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
"""

import sys;
import Checksum;


def main(f1,f2):
    checksum1=Checksum.hasfile(f1);
    checksum2=Checksum.hasfile(f2);

    if checksum1 == checksum2:
        print("Success: Same contents");
    else:
        print("Failure: Do not have same contents..");

if __name__ == "__main__":
    main(str(sys.argv[1]),str(sys.argv[2]));
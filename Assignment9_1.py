"""
Write a program which accepts file name from user and check whether that file exists in
current directory or not.
"""

import sys;
import os;

def main(fileName):

    if os.path.isfile(fileName):
        print("File exists");
    else:
        print("File does not exists");

if __name__ == "__main__":
    main(str(sys.argv[1]));
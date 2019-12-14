"""
Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
"""

import sys;

def main(fileName):

    with open(fileName) as fr:
       with open('Demo.txt','w') as fw:
            fw.write(fr.read())

if __name__ == "__main__":
    main(str(sys.argv[1]));
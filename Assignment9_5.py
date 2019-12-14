"""
Accept file name and one string from user and return the frequency of that string from file.
"""

import sys;


def main(fname,input):
    cnt=0;
    with open(fname,'r') as fr:
        for i in fr:
            i=i.strip();
            i=i.lower();

            words = i.split(" ");
            for word in words:
                if word == input:
                    cnt+=1;
    print(input + " Occured " + str(cnt) + " times in file.");

if __name__ == "__main__":
    main(str(sys.argv[1]),str(sys.argv[2]));
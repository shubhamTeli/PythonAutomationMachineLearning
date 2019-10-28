import sys;

def ChkNum(no):
    if (no % 2 == 0):
       print ("Even number");
    else:
       print ("Odd Number");

def main():
    ChkNum(int(sys.argv[1]));

if (__name__ == '__main__'):
    main();
import sys;

def main(no):
    if (no == 0):
       print ("Zero");
    elif ( no > 0):
       print ("Positive Number");
    else:
        print ("Negative Number")

if (__name__ == '__main__'):
    main(int(sys.argv[1]));
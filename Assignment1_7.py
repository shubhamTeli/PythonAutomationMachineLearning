import sys;

def DivBy5(no):
    if (no % 5 == 0):
        return "true";
    else:
        return "false";

def main():
    print (DivBy5(int(sys.argv[1])));

if (__name__ == '__main__'):
    main();
import sys;

def Add(no1,no2):
    print ("Addition is ",no1+no2);

def main():
    no1=int(sys.argv[1]);
    no2=int(sys.argv[2]);
    Add(no1,no2);

if (__name__=='__main__'):
    main();
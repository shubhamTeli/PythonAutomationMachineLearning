import sys;

def main(no):
    i=0;
    Digitsum=0;
    while (no != 0):
        Digitsum += no % 10;
        no = no // 10;
        i+=1;
    print("Addition of digits in no are: ",Digitsum);


if (__name__ == '__main__'):
    main(int(sys.argv[1]));

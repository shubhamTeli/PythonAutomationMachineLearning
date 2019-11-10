import sys;

def main(no):
    i=0;
    while (no != 0):
        no = int(no / 10);
        i+=1;
    print("Number of digits in no are ",i);


if (__name__ == '__main__'):
    main(int(sys.argv[1]));

import sys;

def main(no):
    i=1;
    while i <= no:
        for j in range(1,no+1):
            print("*",end=" ");
        print();
        i+=1;

if (__name__ == '__main__'):
    main(int(sys.argv[1]));

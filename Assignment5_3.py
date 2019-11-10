import sys;

def display(no):
    if(no!=0):
        print(no, end=" ");
        display(no-1);

def main(no):
    display(no);

if __name__=='__main__':
    main(int(sys.argv[1]));

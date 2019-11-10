import sys;

def display(no):
    if(no!=0):
        display(no-1);
        print(no, end=" ");
def main(no):
    display(no);

if __name__=='__main__':
    main(int(sys.argv[1]));

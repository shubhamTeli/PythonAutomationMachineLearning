import sys;

fact=1;
def displayFact(no):
    if(no!=0):
        global fact;
        fact=fact*no;
        displayFact(no-1);
    else:
        print("Factorial is: ",fact);

def main(no):
    displayFact(no);

if __name__=='__main__':
    main(int(sys.argv[1]));

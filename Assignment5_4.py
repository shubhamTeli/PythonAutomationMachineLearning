import sys;

sum=0;
def displaySum(no):
    if(no!=0):
        global sum;
        sum=sum+(no%10);
        displaySum(int(no/10));
    else:
        print("Summation of no's digit: ",sum);

def main(no):
    displaySum(no);

if __name__=='__main__':
    main(int(sys.argv[1]));

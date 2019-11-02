import sys;

def IsPrime(no):
    i=2;
    prime=1;
    while (i <= no/2):
        if (no % i == 0):
            prime=0;
            break;
        else:
            i+=1;

    if (prime==1):
        print("It is Prime Number");
    else:
        print("It is Not Prime Number");

def main(no):
    IsPrime(no);

if (__name__ == '__main__'):
    main(int(sys.argv[1]));
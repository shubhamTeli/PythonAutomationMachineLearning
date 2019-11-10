import sys;

def fact(no):
    ans=no;
    for i in range(1,no):
        ans=ans*i;
    return ans;

def main(no):
    print("Factorial is ",fact(no));

if (__name__ == '__main__'):
    main(int(sys.argv[1]));

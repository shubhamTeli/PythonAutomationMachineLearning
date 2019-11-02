import sys;
from Arithmatic import *;

def main(no1,no2):
    Add(no1,no2);
    Sub(no1, no2);
    Mult(no1, no2);
    Div(no1, no2);

if (__name__ == '__main__'):
    main(int(sys.argv[1]),int(sys.argv[2]));

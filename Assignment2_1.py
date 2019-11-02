import sys;
import Arithmatic;

def main(no1,no2):
    Arithmatic.Add(no1,no2);
    Arithmatic.Sub(no1, no2);
    Arithmatic.Mult(no1, no2);
    Arithmatic.Div(no1, no2);

if (__name__ == '__main__'):
    main(int(sys.argv[1]),int(sys.argv[2]));
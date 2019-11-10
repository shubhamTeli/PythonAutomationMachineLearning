import sys;

def AddFactors(no):
    i = 1;
    ans = 0;
    while (i <= no/2):
        if (no % i == 0):
            ans = ans + i;
        i += 1;
    return ans;


def main(no):
    print("Addition of factors is ", AddFactors(no));


if (__name__ == '__main__'):
    main(int(sys.argv[1]));



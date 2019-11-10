from functools import *;

def ChkPrime(no):
    i = 2;
    prime = 1;
    while (i <= no / 2):
        if (no % i == 0):
            prime = 0;
            break;
        else:
            i += 1;

    if (prime == 1):
         return 1;
    else:
        return 0;

def MaxNum(no1,no2):
    if(no1>no2):
        return no1;
    else:
        return no2;


def main():
    numArr=list();
    n=input("How many Numbers? ");

    for i in range(int(n)):
        no=input("Enter number:");
        numArr.append(int(no));

    FiltArr=list(filter(ChkPrime,numArr));
    print("Filtered list",FiltArr);

    MapArr=list(map(lambda no: no*2,FiltArr));
    print("Mapped list",MapArr);

    if(len(MapArr)>0):
        Ans=reduce(MaxNum,MapArr);
        print("Reduced Answer is ",Ans);
    else:
        print("There is no answer");

if __name__=='__main__':
    main();
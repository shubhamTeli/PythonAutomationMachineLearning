from functools import *;

def main():
    numArr=list();
    n=input("How many Numbers? ");

    for i in range(int(n)):
        no=input("Enter number:");
        numArr.append(int(no));

    FiltArr=list(filter(lambda no: (no>=70 and no<=90),numArr));
    print("Filtered list",FiltArr);

    MapArr=list(map(lambda no: no+10,FiltArr));
    print("Mapped list",MapArr);

    if(len(MapArr)>0):
        Ans=reduce(lambda no1,no2: no1*no2,MapArr);
        print("Reduced Answer is ",Ans);
    else:
        print("There is no answer");

if __name__=='__main__':
    main();
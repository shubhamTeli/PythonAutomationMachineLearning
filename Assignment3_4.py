def main():
    numArr=list();
    n=input("How many Numbers? ");
    cnt=0;
    for i in range(int(n)):
        no=input("Enter number:");
        numArr.append(int(no));

    fno=int(input("Enter number to find out frequency for?"));
    for i in range(int(n)):
        if(fno==numArr[i]):
            cnt=cnt+1;

    print("Frequency is",cnt);

if __name__=='__main__':
    main();
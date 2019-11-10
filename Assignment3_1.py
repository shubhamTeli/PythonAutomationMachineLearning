def main():
    numArr=list();
    n=input("How many Numbers? ");
    sum=0;
    for i in range(int(n)):
        no=input("Enter number:");
        numArr.append(int(no));
        sum= sum+ numArr[i];

    print("Addition of all elements is:",sum);

if __name__=='__main__':
    main();
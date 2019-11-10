def main():
    numArr=list();
    n=input("How many Numbers? ");

    no=input("Enter number:");
    numArr.append(int(no));
    mini=int(no);

    for i in range(1,int(n)):
        no = input("Enter number:");
        numArr.append(int(no));
        if (numArr[i]<mini):
            mini=numArr[i];

    print("Manimum number from the list is:",mini);


if __name__=='__main__':
    main();
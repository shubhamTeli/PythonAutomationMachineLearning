def main():
    numArr=list();
    n=input("How many Numbers? ");

    no=input("Enter number:");
    numArr.append(int(no));
    max=int(no);

    for i in range(1,int(n)):
        no = input("Enter number:");
        numArr.append(int(no));
        if (numArr[i]>max):
            max=numArr[i];

    print("Maximum number from the list is:",max);


if __name__=='__main__':
    main();
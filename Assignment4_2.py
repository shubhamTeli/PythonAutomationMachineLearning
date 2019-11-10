fptr=lambda a,b: a*b;

def main():
    no1=int(input("Enter Number 1: "))
    no2 = int(input("Enter Number 2: "))
    ans=fptr(no1,no2);
    print("Multiplication is: ",ans);


if(__name__=='__main__'):
    main();

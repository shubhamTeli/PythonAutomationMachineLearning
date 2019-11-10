from MarvellousNum import ChkPrime

def ListPrime():
    numArr=list();
    n=input("How many Numbers? ");
    Primesum=0;
    for i in range(int(n)):
        no=input("Enter number:");
        numArr.append(int(no));
        if(ChkPrime(int(no))==1):
            Primesum=Primesum+numArr[i];
            
    print("Addition of prime Numbers from list is:",Primesum);

if __name__=='__main__':
    ListPrime();
class Arithmatic:

    def __init__(self,number):
        self.value=number;

    def chkPrime(self):
        tmp=Arithmatic(self.value)
        if(tmp.sumFactors()==1):
            return True;
        return False;

    def chkPerfect(self):
        tmp = Arithmatic(self.value)
        if(tmp.sumFactors()==self.value):
            return True;
        return False;

    def sumFactors(self):
        sum=0;
        for i in range(1,self.value):
            if(int(self.value%i)==0):
                sum=sum+i;
        return sum;

    def factors(self):
        tmp=Arithmatic(self.value);
        if (tmp.chkPrime()):
            print("There is no factor of " + str(self.value));
        else:
            for i in range(1,self.value):
                if (int(self.value % i) == 0):
                    print(str(i)+" is factor of "+str(self.value));

def main():

    no=int(input("Enter Number: "));
    obj1=Arithmatic(no);

    if(obj1.chkPrime()):
        print(str(obj1.value) + " is prime number");
    else:
        print(str(obj1.value) + " is not prime number");

    if(obj1.chkPerfect()):
        print(str(obj1.value) + " is perfect number");
    else:
        print(str(obj1.value) + " is not perfect number");
    if (obj1.chkPrime()):
        print("Sum factors of " + str(obj1.value) + " is: 0");
    else:
        print("Sum factors of "+str(obj1.value)+" is: "+str(obj1.sumFactors()));
    obj1.factors();


if __name__=='__main__':
    main();
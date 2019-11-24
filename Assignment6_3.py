class Arithmatic:

    def __init__(self):
        self.value1=0;
        self.Value2=0;


    def accept(self):
        self.value1=int(input("Enter value1: "));
        self.value2=int(input("Enter value2: "));

    def Addition(self):
        return self.value1+self.value2;

    def Substraction(self):
        return self.value1-self.value2;

    def Multiplication(self):
        return self.value1*self.value2;

    def Division(self):
        return self.value1/self.value2;

    def display(self):
        print("Addition is: ",self.Addition());
        print("Substraction is: ",self.Substraction());
        print("Multiplication is: ",self.Multiplication());
        print("Division is: ",self.Division());

def main():
    obj1=Arithmatic();
    obj2=Arithmatic();

    obj1.accept();
    obj1.display();

if __name__=='__main__':
    main();
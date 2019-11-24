class BankAccount:
    ROI = 10.5;
    def __init__(self, custname, value):
        self.name =custname;
        self.amount =value;

    def Deposit(self,value):
        self.amount = self.amount + value;

    def Withdraw(self,value):
        self.amount = self.amount - value;

    def CalculateInterest(self):
        print("Calculated Monthly interest as per ROI is: ",self.amount*((BankAccount.ROI/100)/12));

    def Display(self):
        print("Account Holder Name: ",self.name);
        print("Amount: ", self.amount);
        self.CalculateInterest();

def main():
    obj1 = BankAccount("Amar",2000);
    obj1.Display();
    obj1.Deposit(500);
    print("After Deposit: ");
    obj1.Display();
    obj1.Withdraw(200);
    print("After Withdraw: ");
    obj1.Display();

    obj2 = BankAccount("Sagar",5000);
    obj2.Display();
    obj2.Deposit(700);
    print("After Deposit: ");
    obj2.Display();
    obj2.Withdraw(400);
    print("After Withdraw: ");
    obj2.Display();

if __name__ == "__main__":
    main();
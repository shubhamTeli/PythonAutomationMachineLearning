class Circle:
    PI=3.14;

    def __init__(self):
        self.Radious=0.0;
        self.Area=0.0;
        self.Circumference=0.0;

    def accept(self):
        self.Radious=int(input("Enter Radious of the Circle: "));

    def calculateArea(self):
        self.Area=(Circle.PI*(self.Radious**2));

    def calculateCircumference(self):
        self.Circumference=(2*Circle.PI*self.Radious);

    def display(self):
        print("Radious of the Circle is: ",self.Radious);
        print("Area of the Circle is: ",self.Area);
        print("Circumference of the Circle is: ",self.Circumference);

def main():
    obj1=Circle();
    obj2=Circle();

    obj1.accept();
    obj1.calculateArea();
    obj1.calculateCircumference();
    obj1.display();

    obj2.accept();
    obj2.calculateArea();
    obj2.calculateCircumference();
    obj2.display();

if __name__=='__main__':
    main();
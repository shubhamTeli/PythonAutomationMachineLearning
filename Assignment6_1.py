class Demo:
    value=0;
    def __init__(self,x,y):
        self.no1=x;
        self.no2=y;
    def fun(self):
        print("Inside fun values are:"+str(self.no1) +" "+str(self.no2));

    def gun(self):
        print("Inside gun values are:"+str(self.no1) +" "+str(self.no2));

def main():
    obj1=Demo(11,21);
    obj2=Demo(51,101);
    obj1.fun();
    obj2.fun();
    Demo.gun(obj1);
    Demo.gun(obj2);

if __name__=='__main__':
    main();
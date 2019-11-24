class BookStore:

    NoOfBooks=0;
    def __init__(self,bname,bauthor):
        self.Name=bname;
        self.Author=bauthor;
        BookStore.NoOfBooks+=1;

    def display(self):
        print(str(self.Name)+" by "+str(self.Author)+". "+str(self.NoOfBooks));

def main():
    obj1=BookStore("Linux System Programming","Robert Love");
    obj2=BookStore("C Programming","Dennis Richie");

    obj1.display();
    obj2.display();

if __name__=='__main__':
    main();
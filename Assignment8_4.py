'''
Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.
'''


import threading;

def small(inputString, lock):
    count=0;
    lock.acquire();
    print("\nThread Id: " + str(threading.get_ident()));
    for i in inputString:
      if (i.islower()):
        count = count + 1;
    print("Number of small characters in " + str(inputString) + " : " + str(count));
    lock.release();


def capital(inputString, lock):
    count = 0;
    lock.acquire();
    print("\nThread Id: " + str(threading.get_ident()));
    for i in inputString:
      if (i.isupper()):
        count = count + 1;
    print("Number of capital characters in " +str(inputString)+ " : "+ str(count));
    lock.release();

def digit(inputString, lock):
    count = 0;
    lock.acquire();
    print("\nThread Id: " + str(threading.get_ident()));
    for i in inputString:
      if (i.isdigit()):
        count = count + 1;
    print("Number of digit in " +str(inputString)+ " : "+ str(count));
    lock.release();

if __name__ == "__main__":
    inputString = "ShubhamTeli496";

    print(inputString);
    lock = threading.Lock();
    smallTread = threading.Thread(target=small, args=(inputString, lock));
    capitalThread = threading.Thread(target=capital, args=(inputString, lock));
    digitThread = threading.Thread(target=digit, args=(inputString, lock));

    smallTread.start();
    capitalThread.start();
    digitThread.start();

    smallTread.join();
    capitalThread.join();
    digitThread.join();


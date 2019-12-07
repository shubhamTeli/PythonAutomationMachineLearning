"""
Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer.
Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number.
After execution of both the thread gets completed main thread should display message as “exit from main”.
"""

import threading;

def EvenFactor(number, lock):
    lock.acquire();
    print("\nEven factors of " + str(number) +" are: ");
    for i in range(1,number):
        if(number % i ==0):
            if (i % 2 == 0):
                print(i, end=' ');
    lock.release();


def OddFactor(number, lock):
    lock.acquire();
    print("\nOdd factors of "+ str(number) +" are: ");
    for i in range(1,number):
        if(number % i ==0):
            if (i % 2 == 1):
                print(i, end=' ');
    lock.release();


if __name__ == "__main__":
    number = 20;
    lock = threading.Lock();
    EvenFactorTread = threading.Thread(target=EvenFactor, args=(number, lock));
    OddFactorThread = threading.Thread(target=OddFactor, args=(number, lock));

    EvenFactorTread.start();
    OddFactorThread.start();

    EvenFactorTread.join();
    OddFactorThread.join();

    print("\n\nExit from main");
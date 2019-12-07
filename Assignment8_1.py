"""
Design python application which creates two thread named as even and odd.
Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
"""

import threading;

def Even(number, lock):
    lock.acquire();
    print("\nFirst 10 Even Nos: ");
    for i in range(number):
        if (i % 2 == 0):
            print(i, end=' ');
    lock.release();


def Odd(number, lock):
    lock.acquire();
    print("\nFirst 10 Odd Nos: ");
    for i in range(number):
        if (i % 2 == 1):
            print(i, end=' ');
    lock.release();


if __name__ == "__main__":
    number = 20;
    lock = threading.Lock();
    EvenTread = threading.Thread(target=Even, args=(number, lock));
    OddThread = threading.Thread(target=Odd, args=(number, lock));

    EvenTread.start();
    OddThread.start();

    EvenTread.join();
    OddThread.join();


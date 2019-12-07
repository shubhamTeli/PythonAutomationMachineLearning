"""
Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
"""

import threading;

def thread1(number, lock):
    lock.acquire();
    print("\nNumbers: ");
    for i in range(1,number+1):
        print(i, end=' ');
    lock.release();


def thread2(number, lock):
    lock.acquire();
    print("\nNumbers: ");
    for i in range(number,0,-1):
        print(i, end=' ');
    lock.release();


if __name__ == "__main__":
    number = 50;
    lock = threading.Lock();
    Thread1 = threading.Thread(target=thread1, args=(number, lock));
    Thread2 = threading.Thread(target=thread2, args=(number, lock));

    Thread1.start();
    Thread2.start();

    Thread1.join();
    Thread2.join();


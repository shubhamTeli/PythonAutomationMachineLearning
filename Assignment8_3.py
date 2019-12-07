'''
Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
'''


import threading;

def EvenList(numberList, lock):
    sum=0;
    lock.acquire();
    for i in range(len(numberList)+1):
      if (i % 2 == 0):
        sum = sum + i;
    print("\nAddition of Even elments from list is: " + str(sum));
    lock.release();


def OddList(numberList, lock):
    sum = 0;
    lock.acquire();
    for i in range(len(numberList)+1):
        if (i % 2 == 1):
            sum = sum + i;
    print("\nAddition of Odd elments from list is: " + str(sum));
    lock.release();


if __name__ == "__main__":
    numberList = [1,2,3,4,5,6,7,8,9,10];
    print(numberList);
    lock = threading.Lock();
    EvenListTread = threading.Thread(target=EvenList, args=(numberList, lock));
    OddListThread = threading.Thread(target=OddList, args=(numberList, lock));

    EvenListTread.start();
    OddListThread.start();

    EvenListTread.join();
    OddListThread.join();


import threading
import time
from threading import Thread, Lock
from random import randint, uniform

class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            summ = randint(50, 500)
            self.balance += summ
            print(f'\nПополнение:{summ}. Баланс:{self.balance}')
            time.sleep(uniform(0.01, 0.04))
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            summ = randint(50, 500)
            print(f'\nЗапрос на {summ}.')
            if self.balance >= summ:
                self.balance -= summ
                print(f' Снятие {summ}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
                time.sleep(uniform(0.01, 0.04))


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'\nИтоговый баланс: {bk.balance}')
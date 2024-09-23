import time
from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        # self.run()


    def run(self):
        print(f'{self.name}, на нас напали!')
        for i in range(0, 100, self.power):
            time.sleep(1)
            print(f'{self.name} сражается {int(i/self.power+1)} день(дня)..., осталось {100-i} воинов.')
        return print(f'{self.name} отдержал победу спустя {100/self.power} дней')


thread1 = Knight('Sir Lancelot', 10)
thread2 = Knight("Sir Galahad", 20)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Все битвы кончились!')
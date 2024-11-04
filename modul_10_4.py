from threading import Thread
from time import sleep
from random import randint

class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


tables = [Table(number) for number in range(0, 6)]

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def run(self):
        sleep(randint(3, 10))

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]

class Cafe():

    def __init__(self, queue, *tables):
        import queue
        self.queue = queue.Queue()
        self.tables = list(tables)


    def guest_arrival(self, *guests):

        for guest in guests:
            table_ocup = False

            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    guest.join()
                    print(f'{guest.name} сел(-а)'
                          f' за стол номер {table.number}')
                    table_ocup = True
                    break

            if table_ocup == False:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):

        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:

                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-ла) и ушёл(-ла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел из очереди и сел за стол {table.number}')
                    table.guest.start()
                    table.guest.join()


cafe = Cafe(*tables)

cafe.guest_arrival(*guests)
cafe.discuss_guests()

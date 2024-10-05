import multiprocessing
import datetime


def read_info(*names):
    all_data = []
    for name in names:
        with open(name, 'r') as file:
            while True:
                line = file.readline()
                all_data.append(line)
                if not line:
                    break

start = datetime.datetime.now()
read_info('file 1.txt', 'file 2.txt', 'file 2.txt', 'file 2.txt')
end = datetime.datetime.now()

print(end - start)

#0:00:06.016061
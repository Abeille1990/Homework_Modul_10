import multiprocessing
import datetime


def read_info(name):
    with open(name, 'r') as file:
        all_data = []
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

#############################################################################################

# start = datetime.datetime.now()
# for file in filenames:
#     read_info(file)
# end = datetime.datetime.now()

#############################################################################################

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()

    print(end - start)

#Линейный : 00:00:04.538663
#Многопроцессорный: 0:00:02.679266

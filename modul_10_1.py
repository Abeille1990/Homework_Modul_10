from datetime import datetime
from threading import Thread
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for j in range(int(word_count)):
            file.write(f'Какое-то слово № {j+1}\n')
    print (f'Завершилась запись в файл {file_name}')
    sleep(0.1)

start_time_f = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

stop_time_f = datetime.now()
f_time = stop_time_f - start_time_f
print(f'Работа потоков:  {f_time}')

start_time_t = datetime.now()

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

stop_time_t = datetime.now()
t_time = stop_time_t - start_time_t
print(f'Работа потоков: {t_time}')

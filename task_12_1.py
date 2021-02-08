# Создать программу Pomodoro ( https://ru.wikipedia.org/wiki/Метод_помидора ).
# На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут), длину перерыва(по-
# умолчанию 5 минут), количество циклов(по-умолчанию 4) и название задачи. Программа указывает оставшееся время
# фокусировки, после сигнализирует о наступлении перерыва, после сигнализирует о начале нового цикла фокусировки.
# Программа должна вести фа л лога о всех запусках.

from time import sleep
import argparse
import csv
import datetime
from datetime import timedelta


def my_generator(time1, time2, cycle):
    default_time1 = time1
    default_time2 = time2
    while cycle >= 1:
        print(f'START WORK - CYCLE {cycle}')
        while time1 >= datetime.timedelta(seconds=1):
            sleep(1)
            time1 = time1 - timedelta(seconds=1)
            yield time1
        time1 = default_time1
        print('START BREAK')
        while time2 >= datetime.timedelta(seconds=1):
            sleep(1)
            time2 = time2 - timedelta(seconds=1)
            yield time2
        time2 = default_time2
        cycle -= 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-tf', '--focus', required=True, default=25)
    parser.add_argument('-tb', '--breaks', required=True, default=5)
    parser.add_argument('-c', '--cycle', required=True, default=4)
    parser.add_argument('-n', '--project-name', required=True)
    args = parser.parse_args()
    my_time_focus = datetime.timedelta(seconds=int(args.focus)*60)
    my_time_break = datetime.timedelta(seconds=int(args.breaks)*60)
    cycle = int(args.cycle)
    with open('log.csv', 'a') as my_log:
        writer = csv.writer(my_log)
        writer.writerow([args.first_name, args.last_name, datetime.datetime.today(), args.project_name])
    my_timer = my_generator(my_time_focus, my_time_break, cycle)
    for i in my_timer:
        print(i)


if __name__ == '__main__':
    main()

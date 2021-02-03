# Написать программу таймер. Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратны отсчет выводя оставшееся время. Программа должна хранить файл
# логирования с информацие о том кто запускал программу и когда.

from time import sleep
import argparse
import csv
import datetime
from datetime import timedelta


def my_generator(x):
    while x >= datetime.timedelta(seconds=1):
        sleep(1)
        x = x - timedelta(seconds=1)
        yield x


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-hr', '--hours', required=True)
    parser.add_argument('-m', '--minutes', required=True)
    parser.add_argument('-s', '--seconds', required=True)
    args = parser.parse_args()
    my_time = datetime.timedelta(seconds=int(args.hours) * 3600 + int(args.minutes) * 60 + int(args.seconds))
    with open('log.csv', 'a') as my_log:
        writer = csv.writer(my_log)
        writer.writerow([args.first_name, args.last_name, datetime.datetime.today()])
    my_timer = my_generator(my_time)
    for i in my_timer:
        print(i)


if __name__ == '__main__':
    main()

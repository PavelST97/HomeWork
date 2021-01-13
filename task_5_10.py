# Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время
# отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# (Примечание: использовать возможности библиотеки datetime).

import datetime

x = datetime.datetime(2021, 1, 11, 12, 28)
y = datetime.datetime(2021, 1, 11, 6, 30)
z = datetime.datetime(2021, 1, 11, 12, 47)
h = datetime.datetime(2021, 1, 11, 4, 20)
city_otp = ['Pinsk', 'Minsk', 'Grodno', 'Gomel']
time_otp = [x.strftime('%Y-%m-%d %H.%M'),
            y.strftime('%Y-%m-%d %H.%M'),
            z.strftime('%Y-%m-%d %H.%M'),
            h.strftime('%Y-%m-%d %H.%M')]
otp_time = [x, y, z, h]

x1 = datetime.datetime(2021, 1, 11, 18, 50)
y1 = datetime.datetime(2021, 1, 11, 17, 5)
z1 = datetime.datetime(2021, 1, 11, 23, 15)
h1 = datetime.datetime(2021, 1, 11, 18, 37)
city_pr = ['Mogilev', 'Smorgon', 'Molodechno', 'Minsk']
time_pr = [x1.strftime('%Y-%m-%d %H.%M'),
           y1.strftime('%Y-%m-%d %H.%M'),
           z1.strftime('%Y-%m-%d %H.%M'),
           h1.strftime('%Y-%m-%d %H.%M')]
pr_time = [x1, y1, z1, h1]

train = ['103', '117', '24', '76']

info_list = []
info_dict1 = {gor: vr for gor in city_otp for vr in time_otp}
info_dict2 = {gor2: vr2 for gor2 in city_pr for vr2 in time_pr}
info3 = []
inf1 = list(info_dict1.items())
inf2 = list(info_dict2.items())
for i in range(4):
    info3.append(f'{inf1[i]} - {inf2[i]}')

train_dict = {x: info_dict for x, info_dict in zip(train, info3)}

for i in range(4):
    delta = pr_time[i] - otp_time[i]
    if delta.seconds > 26400:
        print(train[i], train_dict[train[i]])


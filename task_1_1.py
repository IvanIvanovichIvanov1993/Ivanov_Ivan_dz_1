print('Добро пожаловать в программу, которая переводит секунды в минуты, часы, сутки')
duration = int(input('Введите количество секунд '))
if duration / 60 < 1:
    print(duration, 'сек')
elif 1 <= duration / 60 < 60:
    result_min = duration // 60
    result_sek = duration % 60
    print(result_min, 'мин., ', result_sek, 'сек.')
elif 60 <= duration / 60 < 1440:
    result_hours = duration // 3600
    result_min = (duration % 3600) // 60
    result_sek = (duration % 3600) % 60
    print(result_hours, 'час(-а; - ов), ', result_min, 'мин., ', result_sek, 'сек.')
elif duration / 60 >= 1440:
    result_days = duration // 86400
    result_hours = (duration % 86400) // 3600
    result_min = ((duration % 86400) % 3600) // 60
    result_sek = ((duration % 86400) % 3600) % 60
    print(result_days, 'дней, ', result_hours, 'час(-а; - ов), ', result_min, 'мин., ', result_sek, 'сек.')
print('Программа закончена')
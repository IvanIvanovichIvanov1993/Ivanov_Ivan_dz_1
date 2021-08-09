error_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
for elem in error_list:
    elem = elem[::-1]
    elem_new = elem[:elem.index(' ')]
    elem_new = elem_new[::-1]
    elem_new = elem_new.capitalize()
    print('Привет,', elem_new, '!')
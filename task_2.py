list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in list_1:
    if i.isdigit():
        index = (list_1.index(i))
        list_1[index] = i.zfill(2)
    elif i[0] == '+' or i[0] == '-':
        index = (list_1.index(i))
        list_1[index] = i.zfill(3)
print(list_1)
print(' '.join(list_1))
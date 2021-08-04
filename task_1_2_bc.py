list_1 = []
for i in range(1, 1000, 2):
    list_1.append(i ** 3 + 17)
print(list_1)
aggregate_sum = 0
for number in list_1:
    digits_sum = number % 10
    remainder = number // 10
    while remainder > 0:
        digits_sum += remainder % 10
        remainder = remainder // 10
    if digits_sum % 7 == 0:
        aggregate_sum += number
print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, составляет:', aggregate_sum)
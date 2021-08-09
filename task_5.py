# A #
my_prices = [57.8, 46.51, 97, 26.39, 55.17, 122, 5, 77.79, 4.06, 19.1]
for price in my_prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.')

# B #
my_prices = [57.8, 46.51, 97, 26.39, 55.17, 122, 5, 77.79, 4.06, 19.1]
print(id(my_prices))
my_prices.sort()
print(id(my_prices))
for price in my_prices:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.')

# C #

my_prices = [57.8, 46.51, 97, 26.39, 55.17, 122, 5, 77.79, 4.06, 19.1]
my_prices.sort()
my_prices_new = list(reversed(my_prices))
for price in my_prices_new:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.')
print(id(my_prices))
print(id(my_prices_new))

# D #

my_prices = [57.8, 46.51, 97, 26.39, 55.17, 122, 5, 77.79, 4.06, 19.1]
for price in sorted(my_prices)[::-1][:5]:
    rub = int(price)
    kop = (price - rub) * 100
    print(f'{rub} руб. {kop:02.0f} коп.')
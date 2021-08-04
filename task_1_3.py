for n in range(1, 101):
    if n % 10 == 1 and not(11 <= n <= 14):
        print(n, 'процент')
    elif 2 <= n % 10 <= 4 and not(11 <= n <= 14):
        print(n, 'процента')
    elif 5 <= n % 10 <= 9 or n % 10 == 0 or (11 <= n <= 14):
        print(n, 'процентов')
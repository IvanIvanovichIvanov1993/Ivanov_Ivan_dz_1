def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_11 = odd_nums(11)

print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))

# Задание 1*
n = 11
odd_nums = (num for num in range(1, n + 1, 2))
print(next(odd_nums))
print(next(odd_nums))

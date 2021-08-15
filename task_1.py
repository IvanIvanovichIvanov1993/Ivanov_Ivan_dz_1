numerals = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыре', 'five': 'пять', 'six': 'шесть',  'seven': 'семь',
            'eight': 'восемь',  'nine': 'девять', 'ten': 'десять'}
def num_translate(key):
    return numerals.setdefault(key)
print(num_translate('four'))

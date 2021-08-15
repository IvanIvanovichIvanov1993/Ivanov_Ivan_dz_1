nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
import random
def get_jokes(n):
    my_list = []
    """This function to return jokes. n - numbers of jokes"""
    for i in range(n):
        my_string = (random.choice(nouns) + '/' + random.choice(adverbs) + '/' + random.choice(adjectives)).split('/')
        my_list_1 = ' '.join(my_string)
        my_list.append(my_list_1)
    return my_list
print(get_jokes(4))
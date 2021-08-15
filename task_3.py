my_dict = {}
def thesaurus(*args):
    for arg in args:
        my_dict.setdefault(arg[0], [])
        my_dict[arg[0]].append(arg)
    return my_dict
print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
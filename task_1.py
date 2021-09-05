import re

RE_NAME = re.compile(r'^\S\w+[^@]')
RE_DOMAIN = re.compile(r'[^@]\w+\.\w+$')


def email_parse(email):
    if '.' not in ''.join(RE_DOMAIN. findall(email)):
        raise ValueError(f'wrong email: {email}')
    else:
        my_dict = {'username': ''.join(RE_NAME.findall(email)), 'domain': ''.join(RE_DOMAIN.findall(email))}
    return my_dict



print(email_parse('ivanov1993@yandex.ru'))
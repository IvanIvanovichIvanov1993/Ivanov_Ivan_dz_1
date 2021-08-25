from itertools import zip_longest
import json
my_dict = {}
with open('users.csv', encoding = 'utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        sum_users_lines = sum(1 for line in users)
        sum_hobby_lines = sum(1 for line in hobby)
        if sum_hobby_lines < sum_hobby_lines:
            exit(1)

        users.seek(0)
        hobby.seek(0)

        for user_line, hobby_line in zip_longest(users, hobby):
            my_dict[user_line.strip()] = hobby_line.strip() if hobby_line is not None else hobby_line

with open('json_file.json', 'w', encoding='utf-8') as json_file:
    json.dump(my_dict, json_file, ensure_ascii=False)
print(my_dict)
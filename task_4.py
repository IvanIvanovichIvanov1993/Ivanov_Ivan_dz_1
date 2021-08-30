import os
files_size = []
my_dict = {}
for root, dirs, files in os.walk(r'my_project'):
    for file in files:
        file_stat = os.stat(os.path.join(root, file))
        files_size.append(file_stat.st_size)

max_size = max(files_size)

i = 1

for _ in range(len(str(max_size))):
    i *= 10
    my_dict[i] = 0

for size in files_size:
    my_dict[10 ** len(str(size))] += 1
print(my_dict)
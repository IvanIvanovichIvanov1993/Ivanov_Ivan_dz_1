import os
my_list = ['settings', 'mainapp', 'adminapp', 'authapp']
for folder in my_list:
    a = os.path.join('my_project', folder)
    if not os.path.exists(a):
        os.makedirs(a)

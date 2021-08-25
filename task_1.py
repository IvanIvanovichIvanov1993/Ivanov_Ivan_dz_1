with open('C:\\Users\\user\\Desktop\\nginx_logs.txt', 'r', encoding='utf-8') as f:
    my_list = []
    for line in f:
        remote_address = line.split('- -')[0].strip()
        request_type = line.split('"')[1].split('/')[0].strip()
        requested_resource = line.split('"')[1].split()[1]
        a = (remote_address, request_type, requested_resource)
        my_list.append(a)
    print(my_list)

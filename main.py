import os

def create_list(folder):
    file_list = os.listdir(folder)
    tmp_list = {}
    for file in file_list:
        with open('file', 'r') as f:
            t = f.read().count('')

        print(t)
    return print(tmp_list)
create_list('LIST')
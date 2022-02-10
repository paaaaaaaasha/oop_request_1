import os
def create_list(folder):
    file_list = os.listdir(folder)
    sorted_file_list = []
    for file in file_list:
        with open(folder + "/" + file) as _tmp_list:
            sorted_file_list.append([file, 0, []])
            for line in _tmp_list:
                sorted_file_list[-1][2].append(line.strip())
                sorted_file_list[-1][1] += 1
    sorted_file_list=sorted(sorted_file_list, key=lambda x: x[1], reverse=False)
    with open('by_sorted' + '.txt', 'w+') as sorted_file:
        sorted_file.write(f'Даны файлы:\n')
        for file in sorted_file_list:
            sorted_file.write(f'Назввание файла: {file[0]}\n')
            sorted_file.write(f'Количество строк: {file[1]}\n')
            for string in file[2]:
                sorted_file.write(string + '\n')
            sorted_file.write('\n')
    return print('File sorted')

create_list('LIST')
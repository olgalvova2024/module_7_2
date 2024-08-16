def custom_write(file_name, strings):
    file = open(file_name,'a', encoding='utf-8')
    strings_positions = {}
    line_number = 1
    for i in strings:
        strings_positions[(line_number,file.tell())] = i
        line_number += 1
        file.write(i)
        file.write('\n')
    file.close()
    return strings_positions


info = ['Text for tell.','Используйте кодировку utf-8.','Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
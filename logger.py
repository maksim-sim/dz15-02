from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком варианте записать данные?\n'
                    f'1 - Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 - Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл: ')
    with open('data_first.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

    print('2 файл: ')
    with open('data_second.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))


def delete_data():
    file_num = int(input('Введите номер файла (1 или 2): '))
    while file_num not in [1, 2]:
        file_num = int(input('Ошибка! Введите номер файла (1 или 2): '))

    line_num = int(input('Введите номер строки, которую нужно удалить: '))
    while line_num < 1:
        line_num = int(input('Ошибка! Введите номер строки, которую нужно удалить: '))

    if file_num == 1:
        with open('data_first.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        if line_num <= len(data):
            data.pop(line_num - 1)
            with open('data_first.csv', 'w', encoding='utf-8') as file:
                file.writelines(data)
            print('Строка успешно удалена.')
        else:
            print('Ошибка! Нет строки с таким номером.')
    else:
        with open('data_second.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        if line_num <= len(data):
            data.pop(line_num - 1)
            with open('data_second.csv', 'w', encoding='utf-8') as file:
                file.writelines(data)
            print('Строка успешно удалена.')
        else:
            print('Ошибка! Нет строки с таким номером.')


def edit_data():
    file_num = int(input('Введите номер файла (1 или 2): '))
    while file_num not in [1, 2]:
        file_num = int(input('Ошибка! Введите номер файла (1 или 2): '))

    line_num = int(input('Введите номер строки, которую нужно изменить: '))
    while line_num < 1:
        line_num = int(input('Ошибка! Введите номер строки, которую нужно изменить: '))

    new_data = input('Введите новые данные: ')

    if file_num == 1:
        with open('data_first.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        if line_num <= len(data):
            data[line_num - 1] = new_data + '\n'
            with open('data_first.csv', 'w', encoding='utf-8') as file:
                file.writelines(data)
            print('Строка успешно изменена.')
        else:
            print('Ошибка! Нет строки с таким номером.')
    else:
        with open('data_second.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        if line_num <= len(data):
            data[line_num - 1] = new_data + '\n'
            with open('data_second.csv', 'w', encoding='utf-8') as file:
                file.writelines(data)
            print('Строка успешно изменена.')
        else:
            print('Ошибка! Нет строки с таким номером.')
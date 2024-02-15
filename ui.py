from logger import input_data, print_data, delete_data, edit_data


def interface():
    print('добрый день! это бот помощник. \n'
          'что вы хотите сделать? \n'
          '1 - записать данные \n'
          '2 - вывести данные \n'
          '3 - удалить данные \n'
          '4 - изменить данные')
    command = int(input('ваш выбор: '))

    while command < 1 or command > 4:
        command = int(input('ошибка! ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        edit_data()

interface()
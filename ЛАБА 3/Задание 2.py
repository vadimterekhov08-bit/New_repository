text = input('Введите текст для добавления в файл: ')

def append_to_file(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text)
    print(f'Текст добавлен в файл {file_name}.')

def write_to_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)
    print(f'Текст записан в файл {file_name}.')

file_name = 'user_input.txt'
choise = input('Выберите метод (1 - Добавить, 2 - Записать): ')

if choise == '1':
    append_to_file(file_name, text)
elif choise == '2':
    write_to_file(file_name, text)
else:
    print('Неверный выбор')

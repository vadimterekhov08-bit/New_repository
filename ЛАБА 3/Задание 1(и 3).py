tip = input('Выберите тип чтения(all или lines): ')
try:
    with open('example.txt', 'r') as file:
        if tip == 'all':
            content = file.read()
            print(content)
        elif tip == 'lines':
            for line in file:
                print(line.strip())
        else: 
            print('Неверный тип чтения')
except FileNotFoundError:
    print('Файл не найден')
import sys
import os

import my_modules as my

choice = 0

while choice != '5':
    print('''
    1. Перейти в папку
    2. Просмотреть содержимое папки
    3. Удалить папку
    4. Создать папку
    5. Выйти из программы
    ''')

    choice = input('Введите номер пункта, который хотите выполнить: ')

    if choice == '1':
        dir_name = input('Введите название папки: ')
        my.ch_dir(dir_name)
    elif choice == '2':
        my.list_dir()
    elif choice == '3':
        dir_name = input('Введите название папки: ')
        my.del_dir(dir_name)
    elif choice == '4':
        dir_name = input('Введите название папки: ')
        my.add_dir(dir_name)

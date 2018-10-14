import os
import shutil

'''
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
 
# копия текущего файла
'''
    
def copy_cwd():
    shutil.copy(r'L5_Task3_easy.py', r'L5_Task3_easy_dupl.py')

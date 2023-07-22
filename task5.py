# Напишите функцию, которая ищет json файлы в указанной директории и 
# сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle
import os

def convert_json_pickle():
    all_files_json = (file for file in os.listdir('.') if file.endswith('.json'))
    for file_json in all_files_json:
        with open(file_json, 'r', encoding='utf-8') as fj:
            dict_user = json.load(fj)
        
        name_new_file = file_json.split('.')[0]
        file_pickle = name_new_file + '.' + 'pickle'
            
        with open(file_pickle, 'wb') as f_p:
            pickle.dump(dict_user, f_p)
    
        
if __name__ == '__main__':
    
    convert_json_pickle()
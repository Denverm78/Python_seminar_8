# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и 
# все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию (parent_dir).
# ○ Для каждого объекта укажите файл это или директория (type).
# ○ Для файлов сохраните его размер в байтах (size), а для директорий размер файлов в ней 
# с учётом всех вложенных файлов и директорий (size).
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы 
# с файлами разных форматов.

from pathlib import Path
import json
import pickle
import csv

def get_dict_obj_info(current_file):
    dict_obj_info = {}
    dict_obj_info['file_name'] = Path(current_file).name
    dict_obj_info['parent_dir'] = Path(current_file).parent.name
    if Path(current_file).is_file():
        dict_obj_info['type'] = 'file'
        dict_obj_info['size'] = Path(current_file).stat().st_size
    else:
        dict_obj_info['type'] = 'dir'
        dict_obj_info['size'] = 0
        child_list_dir = []
        for file in Path(current_file).iterdir():
            child_dir = get_dict_obj_info(file)
            dict_obj_info['size'] = dict_obj_info['size'] + child_dir.get('size', 0)
            child_list_dir.append(child_dir)
        dict_obj_info['child'] = child_list_dir
    return dict_obj_info

def create_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_pickle(data, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)

def create_csv(data, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        list_headers = ['file_name','parent_dir', 'type', 'size']
        csw_writer = csv.DictWriter(f, fieldnames=list_headers, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        csw_writer.writeheader()
        data_list = []
        convert_dict_list(data, data_list)

        csw_writer.writerows(data_list)

def convert_dict_list(data_dict, data_list):
    user_dict = {'file_name': data_dict.get('file_name', ""),
        'parent_dir': data_dict.get('parent_dir', ""),
        'size': data_dict.get('size', 0),
        'type': data_dict.get('type', "")}
    data_list.append(user_dict)
    child_list = data_dict.get('child', None)
    if child_list is not None:
        for name in child_list:
            convert_dict_list(name, data_list)
    return data_list

if __name__ == '__main__':
    
    user_path = input('Введите полный путь к файлу или директории: ')
    # user_path = 'L:\Обучение'
    json_file = 'result.json'
    csv_file = 'result.csv'
    pickle_file = 'result.pickle'
    result_dict = get_dict_obj_info(user_path)
    create_json(result_dict, json_file)
    create_pickle(result_dict, pickle_file)
    create_csv(result_dict, csv_file)
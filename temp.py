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
        dict_child_dir = {}
        for file in Path(current_file).iterdir():
            child_dir = get_dict_obj_info(file)
            dict_obj_info['size'] += child_dir.get('size', 0)
            dict_child_dir[current_file] = child_dir
        dict_obj_info['child'] = dict_child_dir

    return dict_obj_info

print(get_dict_obj_info('f:\SEM_8'))
# if __name__ == '__main__':
    
    # user_path = input('Введите полный путь к файлу или директории')

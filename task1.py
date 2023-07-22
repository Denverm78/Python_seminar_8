""" Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
📌 Имена пишите с большой буквы.
📌 Каждую пару сохраняйте с новой строки. """

import json

def convert_txt_json(file_name):
    user_dict = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        while user_str := f.readline():
            user_str = user_str.replace("('", '').replace("'",'').replace(' \n', '').replace(")","")
            key, value = user_str.split(', ')
            user_dict[key.capitalize()] = float(value)
    print(user_dict)
    with open('new_user.json', 'w', encoding='utf-8') as f_json:
        json.dump(user_dict, f_json, indent=2, ensure_ascii=False)        

file_name = 'result.txt'

if __name__ == '__main__':

    convert_txt_json(file_name)


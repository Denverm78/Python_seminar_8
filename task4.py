# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json

def convert_csv_json(file_csv, file_json):
    list_json = []
    with open(file_csv, 'r', encoding='utf-8') as fc:
        reader = csv.reader(fc)
        for i, list_str in enumerate(reader):
            if i != 0:
                dict_json = {}
                user_level, user_id, user_name = list_str
                dict_json['user_level'] = user_level
                dict_json['user_id'] = user_id.zfill(10)
                dict_json['user_name'] = user_name.title()
                dict_json['hash'] = hash(f'{user_id}{user_name}')
                list_json.append(dict_json)
            else:
                continue

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(list_json, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    
    convert_csv_json('file_task4.csv', 'file_task4.json')
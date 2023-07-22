# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json

def convert_json_csv():
    with open('date_users.json', 'r', encoding='utf-8') as read_f:
        dict_levels = json.load(read_f)
        list_dict = []
        for level, value in dict_levels.items():
            for id, name in value.items():
                list_dict.append({'user_level': level, 'user_id': id, 'user_name': name})
        print(list_dict)
    
    with open('date_users.csv', 'w', newline='', encoding='utf-8') as write_f:
        csv_write = csv.DictWriter(write_f, fieldnames=['user_level','user_id','user_name'], dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(list_dict)


if __name__ == '__main__':

    convert_json_csv()
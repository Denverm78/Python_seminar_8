# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import json

def create_users_json():
    MIN_LEVEL = 1
    MAX_LEVEL = 7
    while True:
        with open('date_users.json', 'r', encoding='utf-8') as d_u:
            dict_levels = json.load(d_u)
        user_name = input("Введите имя пользователя: ")
        user_id = input("Введите личный идентификатор: ")
        user_level = input(f"Введите уровень доступа от {MIN_LEVEL} до {MAX_LEVEL}: ")
        values_list = []
        for value in dict_levels.values():
            for key in value:
                values_list.append(key)
        if user_id not in values_list:
            dict_users = dict_levels[user_level]
            dict_users[user_id] = user_name
            dict_levels[user_level] = dict_users
        else:    
            print("Такой id уже существует")
            
                    
        with open('date_users.json', 'w', encoding='utf-8') as f:
            json.dump(dict_levels, f, indent=2, ensure_ascii=False)
            
if __name__ == '__main__':            

    create_users_json()
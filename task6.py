# Напишите функцию, которая преобразует pickle файл, хранящий список словарей 
# в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv

def convert_pickle_csv(file_pickle):
    
    name_new_file = file_pickle.split('.')[0]
    file_csv = name_new_file + '_6' + '.' + 'csv'
        
    with open(file_pickle, 'rb') as f_p:
        data = pickle.load(f_p)
        list_headers = []
        print(data[0])
        for key in data[0].keys():
            list_headers.append(key)
        print(list_headers)
            
    with open(file_csv, 'w', encoding='utf-8') as f_c:
        csv_write = csv.DictWriter(f_c, fieldnames=list_headers, dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(data)
       
        
if __name__ == '__main__':            
            
    file_pickle = 'file_task4.pickle'
    convert_pickle_csv(file_pickle)

# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import pickle
import csv

def print_csv_as_picklestr(file_csv):
    with open(file_csv, 'r', encoding='utf-8') as f_c:
        data_csv = f_c.read()
        print(pickle.dumps(data_csv))
    

if __name__ == '__main__':   

    file_csv = 'file_task4_6.csv'    
    print_csv_as_picklestr(file_csv)
from pprint import pprint
import re
import csv
from applications.list_to_dicts import make_dict
from applications.dicts_to_list import create_contact_list_correct

if __name__ == '__main__':
    ## Читаем адресную книгу в формате CSV в список contacts_list:
    with open("data/phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    a, a1, a2, a3, a4 = make_dict(contacts_list)
    new_contact_list = create_contact_list_correct(a, a1, a2, a3, a4)

    ## Код для записи файла в формате CSV:
    with open("data/phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_contact_list)
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv",encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)


#(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*(доб.)*\s*(\d+)*\)*
#+7(\2)\3-\4-\5 \6\7
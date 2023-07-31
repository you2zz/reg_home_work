from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

surnames = {}
organizations = {}
positions = {}
phones = {}
emails = {}

pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*(доб.)*\s*(\d+)*\)*"
replace = r"+7(\2)\3-\4-\5 \6\7"

for i in contacts_list:
  i_0 = i[0].split()
  i_1 = i[1].split()
  organization = i[3]  
  position = i[4]  
  phone = re.sub(pattern, replace, i[5])
  email = i[6] 
  if len(i_0) == 3:
    last_first_name = f'{i_0[0].strip()} {i_0[1].strip()}'
    surname = f'{i_0[2].strip()}'
    if last_first_name not in surnames:
      surnames[last_first_name] = surname
  elif len(i_0) == 2:
    last_first_name = f'{i_0[0].strip()} {i_0[1].strip()}'
    surname = i[2].strip()
    if last_first_name not in surnames:
      surnames[last_first_name] = surname
  else:
    if len(i_1) == 2:
      last_first_name = f'{i[0].strip()} {i_1[0].strip()}'
      surname = f'{i_1[1].strip()}'      
    else:
      last_first_name = f'{i[0].strip()} {i[1].strip()}'
      surname = f'{i[2].strip()}'
    if last_first_name not in surnames:
        surnames[last_first_name] = surname
  if last_first_name not in organizations: # словарь с организациями
    organizations[last_first_name] = organization
  else:
    if organization != '':
      organizations[last_first_name] = organization
  if last_first_name not in positions: # словарь с должностями
    positions[last_first_name] = position
  else:
    if position != '':
      positions[last_first_name] = position
  if last_first_name not in phones: # словарь с телефонами
    phones[last_first_name] = phone
  else:
    if phone != '':
      phones[last_first_name] = phone
  if last_first_name not in emails: # словарь с почтой
    emails[last_first_name] = email
  else:
    if email != '':
      emails[last_first_name] = email




new_contact_list = []
for k, v in surnames.items():
  entry = []
  entry.append(k.split()[0])
  entry.append(k.split()[1])
  entry.append(v)
  entry.append(organizations[k])
  entry.append(positions[k])
  entry.append(phones[k])
  entry.append(emails[k])
  new_contact_list.append(entry)

print(new_contact_list)
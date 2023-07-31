from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)



# contacts_list2=[]

# for i in contacts_list:
#   new_i = ['', '', '', '', '', '', '']
#   i_0 = i[0].split()
#   i_1 = i[1].split()
#   if len(i_0) == 3:
#     for idx, _ in enumerate(new_i):
#       if idx < 3:
#         new_i[idx] = i_0[idx].strip()
#       else:
#         new_i[idx] = i[idx]    
#   elif len(i_0) == 2:
#     for idx, _ in enumerate(new_i):
#       if idx < 2:
#         new_i[idx] = i_0[idx].strip()
#       else:
#         new_i[idx] = i[idx]   
#   else: 
#     if len(i_1) == 2:
#       for idx, _ in enumerate(new_i):
#         if idx < 3 and idx != 0:
#           new_i[idx] = i_1[idx - 1].strip()
#         else:
#           new_i[idx] = i[idx]
#     else:
#       for idx, _ in enumerate(new_i):
#         new_i[idx] = i[idx]
#   contacts_list2.append(new_i)

# pprint(contacts_list2)
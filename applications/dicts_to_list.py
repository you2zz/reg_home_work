def create_contact_list_correct(surnames, organizations, positions, phones,  emails):
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
    return new_contact_list
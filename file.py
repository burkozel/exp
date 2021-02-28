import csv, re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list

def create_new_list(notrightlist):
    rightlist = {}
    for contact in notrightlist:
        zamena = re.compile("\s{2,}|\s{1,}$")
        contact[0:3] = re.sub(zamena, '', ' '.join(contact[0:3])).split(' ')
        new = "+7(\\1)\\2-\\3-\\4"
        add1 = "\\1"
        add = re.compile("\(?(доб\.\s[0-9]{4})\)?")
        all = re.compile("\+?7?8?\s?\(?([0-9]{3})\)?"
                                   "\-?\s?([0-9]{3})"
                                   "\-?([0-9]{2})"
                                   "\-?([0-9]{2})"
        )
        contact[5] = re.sub(all, new, contact[5])
        contact[5] = re.sub(add, add1, contact[5])
        name = contact[1] + contact[0]

        if name not in rightlist:
            rightlist[name] = contact
        else:
            for i, data in enumerate(contact):
                if data != '':
                    rightlist[name][i] = data

    return list(rightlist.values())


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts = list(rows)
    pprint(contacts)

    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="UTF-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(create_new_list(contacts))
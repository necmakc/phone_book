phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for contact in data:
        uid, name, phone, comment = contact.strip().split(';')
        phone_book[int(uid)] = [name, phone, comment]

def save_file():
    with open(path, 'w', encoding='utf-8') as file:
        all_contacts = []
        for uid, contact in phone_book.items():
            all_contacts.append(';' .join([str(uid), contact[0], contact[1], contact[2]]))
        all_contacts = '\n'.join(all_contacts)
        file.write(all_contacts)

def add_contact(new: list[str]) -> str:
    uid = max(phone_book) + 1
    phone_book[uid] = new

def search(word):
    result = {}
    for uid, contact in phone_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[uid] = contact
                break
    return result

def delete_contact(uid:int) -> str:
    return phone_book.pop(uid)[0]

def change_contact(uid: int, rename: list[str]):
    contact = phone_book.get(uid)
    for i in range(3):
        if rename[i]:
            contact[i] = rename[i]
    phone_book[uid] = contact
    return contact[0]
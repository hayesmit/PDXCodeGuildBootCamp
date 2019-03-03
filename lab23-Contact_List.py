# lab23-Contact_List.py

return_contacts = []
contacts = []
with open("contacts.csv", "r") as file:
    lines = file.read().split("\n")
    keys = lines.pop(0).split(',')
    data_points = len(lines[0].split(","))
    for d in range(data_points):
        values = lines[d].split(',')
        new_contact = dict(zip(keys, values))
        contacts.append(new_contact)


def update_contacts():
    save = [','.join(keys)]
    for user in contacts:
        row = user.values()
        ','.join(row)
        save.append(row)
    final_save = '\n'.join(save)
    with open('contacts.csv', 'w') as f:
        f.write(final_save)

def add_contact(name, favorite_fruit, favorite_color):
    values = [name, favorite_fruit, favorite_color]
    contacts.append(dict(zip(keys, values)))
    print(contacts)

def find_information(person):
    for i in contacts:
        if person == i['name']:
            print(i)

#add_contact('jim bob', 'peaches', 'gray')
#find_information('Matt')

def update(user):
    for i in contacts:
        if user == i['name']:
            change = input("what attribute do you want to update? >>"  )
            change_to = input("what would you like to change it to? >> ")
            i[change] = change_to
    print(contacts)


def delete_user(name):
    for i in contacts:
        if i['name'] == name:
            get_out = contacts.index(i)
            contacts.pop(get_out)


updated_contacts()
print(return_contacts)
print(contacts)

# lab23-Contact_List.py


contacts = []
with open("contacts.csv", "r") as file:
    lines = file.read().split("\n")
    keys = lines.pop(0).split(',')
    data_points = len(lines[0].split(","))
    for d in range(data_points):
        values = lines[d].split(',')
        new_contact = dict(zip(keys, values))
        contacts.append(new_contact)
    print(keys)
    print(lines)
    print(contacts)
    print(print)

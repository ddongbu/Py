dict_PhoneBook = {}

for i in range(1, 3):
    name = input("이름:")
    if name == '':
        break
    phone = input("연락처:")
    dict_PhoneBook[name] = phone

print("====연락처목록====")
for name, phone in dict_PhoneBook.items():
    print(f"{name}: {phone}")
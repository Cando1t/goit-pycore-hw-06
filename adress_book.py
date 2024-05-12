from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def validate_phone(self):
        return len(str(self.value)) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj.validate_phone():
            self.phones.append(phone_obj)
        else:
            print("Неправильний номер телефону")

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        found_phones = [p for p in self.phones if str(p) == phone]
        return found_phones[0] if found_phones else None

    def __str__(self):
        phones_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

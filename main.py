def parse_input(user_input):
    tokens = user_input.split()
    
    if not tokens:
        return None, None
    
    command = tokens[0].lower()
    
    arguments = tokens[1:]
    
    return command, arguments

def main():
    contacts = {}
    
    while True:
        user_input = input("Введіть команду: ")
        
        command, arguments = parse_input(user_input)
        
        if command == "exit" or command == "close":
            print("До побачення!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(arguments) != 2:
                print("Неправильний формат команди. Використовуйте: add [ім'я] [номер телефону]")
            else:
                name, phone = arguments
                contacts[name] = phone
                print("Контакт додано.")
        elif command == "change":
            if len(arguments) != 2:
                print("Неправильний формат команди. Використовуйте: change [ім'я] [новий номер телефону]")
            else:
                name, new_phone = arguments
                if name in contacts:
                    contacts[name] = new_phone
                    print("Контакт оновлено.")
                else:
                    print("Контакт з таким ім'ям не знайдено.")
        elif command == "phone":
            if len(arguments) != 1:
                print("Неправильний формат команди. Використовуйте: phone [ім'я]")
            else:
                name = arguments[0]
                if name in contacts:
                    print(f"Номер телефону {name}: {contacts[name]}")
                else:
                    print("Контакт з таким ім'ям не знайдено.")
        elif command == "all":
            print("Всі збережені контакти:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Невідома команда. Спробуйте ще раз.")
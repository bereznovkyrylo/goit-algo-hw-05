from handlers import parse_user_input,add_contact,update_contact,show_phone,show_all
def main():
    contacts={}
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input=input('Enter a command: ').strip().lower()
            command,*args=parse_user_input(user_input)

            if command in ['exit','close']:
                print('Goodbye!')
                break
            elif command=='hello':
                print('How can I help you? ')

            elif command=='add' :
                print(add_contact(args,contacts))

            elif command=='change':
                print(update_contact(args,contacts))

            elif command=='phone':
                print(show_phone(args[0],contacts))

            elif command=='all':
                print(show_all(contacts))
            else:
                print("Invalid command.")
    except Exception as e:
        print(f'{e} with file')



if __name__=='__main__':
    main()
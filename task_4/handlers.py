
def input_error(func):
    def inner(*args,**kwargs):
        try:
           return func(*args,**kwargs)
        except ValueError:
            return 'Enter the argument for the command'
        except KeyError:
            return 'Wrong command'
        except IndexError:
            return 'Enter the argument for the command'
        except Exception as e:
            return f'Error: {e}'
    return inner

@input_error
def parse_user_input(string):
    command,*args=string.split()
    return command,*args

@input_error
def add_contact(args,contacts):                
    name=args[0]
    is_exist_contact=contacts.get(name,None)

    if is_exist_contact is not None:
        answer=input(f'Contact with name {name} already exist. Do you want to update contact? y/n ').strip().lower()
        if answer=='y':
            return update_contact(args,contacts)
        elif answer!='n':
            raise KeyError

    else:            
        name,phone=args
        contacts[name]=phone
        return "Contact added."

@input_error
def update_contact(args,contacts):
    name,phone=args

    contacts[name]=phone
    return "Contact updated."
@input_error
def show_phone(name,contacts):
    return contacts[name]
@input_error
def show_all(contacts):
    return list(contacts.items())

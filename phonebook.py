contacts = {}

while True:
    print('\n .......Welcome to PhoneBook......')
    print('1. Create new contact')
    print('2. Update contact')
    print('3. View contact')
    print('4. Search contact')
    print('5. Delete contact')

    user_choice = int(input('Enter your Choice = '))

    if user_choice == 1:
        name = input('Enter name to create contact  =  ')
        if name in contacts:
            print(f'Contact {name} already exists in Phonebook')
        else:
            address = input('Enter address =  ')
            email = input('Enter email = ')
            phone = input('Enter mobile number = ')
            contacts[name] = {'address': address,'email': email,'phone': phone}
            print(f'Contact created...')

    elif user_choice == 3:
        name = input('Enter name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name},Address:{address},Email:{email},Phone:{phone}')
        else:
            print('Contact not found!!')

    elif user_choice == 2:
        name = input('Enter name to update = ')
        if name in contacts:
            address = input('Enter updated address = ')
            email = input('Enter updated email = ')
            phone = input('Enter updated mobile number = ')
            contacts[name] = {'address':address,'email':email,'phone':phone}
        else:
            print('Contact not found!!')

    elif user_choice == 5:
        name = input('Enter name to delete = ')
        if name in contacts:
            del contacts[name]
            print('Contact has been deleted!!')
        else:
            print('contact not found')

    elif user_choice == 4:
        search_name= input('Enter name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Name {name},Address {address},Email {email},Phone {phone}')
                found = True
            if not found:
                print('No contact in phonebook')

    elif user_choice == 6:
        break

    else:
        print('Invalid input')
        

import view
import model


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('File is opened successfully')
            case 2:
                model.save_file()
                view.show_message('File is saved successfully')
            case 3:
                view.show_contacts(pb, 'Phonebook is empty')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Phonebook is empty'):
                    index = view.input_index('Input the number of contact')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Contact {model.get_phone_book()[index-1].get("name")} is changed successfully!')
            case 6:
                search=view.input_search('Input element you need: ')
                result=model.find_contact(search)
                view.show_contacts(result, 'Contacts are not found')
            case 7:
                return


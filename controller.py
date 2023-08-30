from model import PhoneBook
import text
import view

def search_contact(pb):
    word = view.input_request(text.input_search_word)
    result = pb.find_contact(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True

def save_file(pb):
    pb.save_file()
    view.print_message(text.file_succesful(text.action_file[2]))


def start():
    pb = PhoneBook()
    
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pb.create_file()
                view.print_message(text.file_succesful(text.action_file[0]))
            case 2:
                pb.open_file()
                view.print_message(text.file_succesful(text.action_file[1]))
            case 3:
                save_file(pb)
            case 4:
                view.show_book(pb, text.empty_book_error)
            case 5:
                new_contact = view.input_contact(text.input_contact)
                pb.add_contact(new_contact)
                view.print_message(text.contact_action(new_contact[0], text.operation[0]))
            case 6:
                search_contact(pb)
            case 7:
                if search_contact(pb):
                    c_id = int(view.input_request(text.input_edit_contact_id))
                    new_contact = view.input_contact(text.input_edit_contact)
                    name = pb.edit_contact(c_id, new_contact)
                    view.print_message(text.contact_action(name, text.operation[1]))
            case 8:
                if search_contact(pb):
                    c_id = int(view.input_request(text.input_edit_contact_id))
                    name = pb.delete_contact(c_id)
                    view.print_message(text.contact_action(name, text.operation[2]))
            case 9:
                if pb.original_book != pb.phone_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        save_file(pb)
                view.print_message(text.exit_program)
                break
import model
import text
import view


def search_contact():
    word = view.input_request(text.input_search_word)
    result = model.find_contact(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True


def save_file():
    model.save_file()
    view.print_message(text.file_succesful(text.action_file[2]))


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.create_file()
                view.print_message(text.file_succesful(text.action_file[0]))
            case 2:
                model.open_file()
                view.print_message(text.file_succesful(text.action_file[1]))
            case 3:
                save_file()
            case 4:
                view.show_book(model.phone_book, text.empty_book_error)
            case 5:
                new_contact = view.input_contact(text.input_contact)
                model.add_contact(new_contact)
                view.print_message(text.contact_action(new_contact[0], text.operation[0]))
            case 6:
                search_contact()
            case 7:
                if search_contact():
                    c_id = int(view.input_request(text.input_edit_contact_id))
                    new_contact = view.input_contact(text.input_edit_contact)
                    name = model.edit_contact(c_id, new_contact)
                    view.print_message(text.contact_action(name, text.operation[1]))
            case 8:
                if search_contact():
                    c_id = int(view.input_request(text.input_edit_contact_id))
                    name = model.delete_contact(c_id)
                    view.print_message(text.contact_action(name, text.operation[2]))
            case 9:
                if model.original_book != model.phone_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        save_file()
                view.print_message(text.exit_program)
                break
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from components.notes.notes import RecordNote, NoteData
from components.contacts.contacts import RecordContact, AddressBook

from colorama import *

init(autoreset=True)

COMMANDS = [
    "hello",
    "close",
    "help",
    "add_contact name phone",
    "add_address name address",
    "add_email name email",
    "add_birthday name birthday(DD.MM.YYYY)",
    "change_address name new_address",
    "change_email name new_email",
    "change_contact_phone name phone",
    "delete_contact name",
    "all_contacts",
    "find_contact name || address || phone || email || birthday(DD.MM.YYYY)",
    "contacts_birthdays days(int)",
    "find_notes TITLE || text || date",
    "add_note TITLE text *your #tags*",
    "delete_note TITLE",
    "change_note_title TITLE NEW_TITLE",
    "change_note_text TITLE new_text",
    "add_note_tags TITLE *your tags*",
    "delete_note_tag TITLE #Tag",
    "change_note_tag TITLE #tag #new_tag",
    "find_note_tag *your #tags*",
    "sort_note_tag *your #tags*",
]
COMMANDS_TEST = WordCompleter(
    COMMANDS,
    ignore_case=True,
)

contacts = AddressBook()
notes = NoteData()
FILENAME_CONTACTS = "contacts.json"
FILENAME_NOTES = "notes.csv"


def _parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    if len(args) < 1 and cmd not in ("hello", "close", "help", "all_contacts"):
        print(Fore.LIGHTRED_EX + "Error: Command is missing required arguments.")
    return cmd, *args


def _input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return Fore.LIGHTMAGENTA_EX + "Wrong count of arguments"
        except TypeError:
            return Fore.LIGHTRED_EX + "TypeError"
        except IndexError:
            return Fore.LIGHTRED_EX + "IndexError"
        except AttributeError:
            return Fore.LIGHTRED_EX + "AttributeError"
        except:
            return "Unknow Error"

    return inner


def close_bot():
    contacts.save_to_file(FILENAME_CONTACTS)
    notes.write_csv_file(FILENAME_NOTES)
    print(Fore.LIGHTYELLOW_EX + "Good bye!")


def helloBot():
    print(Fore.LIGHTYELLOW_EX + "How can I help you?")


def helpBot():
    for i in COMMANDS:
        print(f"{i}")


@_input_error
def add_contact(args):
    name, phone = args
    record = RecordContact(name)
    print("ADD PHONE")
    record.add_phone(phone)
    print("RECORD TIME")
    contacts.add_record(record)
    print("Contact added.")


@_input_error
def change_contact_phone(args):
    name, phone = args
    contact = contacts.find(name)
    res = contact.edit_phone(phone)
    print(res)


@_input_error
def delete_contact(args):
    name = args[0]

    print(name)


@_input_error
def find_contact(args):
    name = args[0]
    found_contacts = contacts.search_contacts(name)
    if found_contacts:
        for contact in found_contacts:
            print(contact)
    else:
        print(Fore.LIGHTMAGENTA_EX + "No contacts found.")


@_input_error
def add_address(args):
    name, address = args
    contact = contacts.find(name)
    contact.add_address(address)
    print("Contact updated.")


@_input_error
def change_address(args):
    name, address = args
    contact = contacts.find(name)
    res = contact.edit_address(address)
    print(res)


@_input_error
def add_email(args):
    name, email = args

    contact = contacts.find(name)
    contact.add_email(email)

    print("Email updated.")


@_input_error
def add_birthday(args):
    name, birthday = args
    contacts.add_birthday(name, birthday)
    print("Birthday updated.")


@_input_error
def change_email(args):
    name, email = args
    contact = contacts.find(name)
    res = contact.edit_email(email)
    print(res)


@_input_error
def all_contacts():
    res = Fore.MAGENTA + "\nAll Contacts:\n" + Fore.WHITE
    for key, value in contacts.items():
        res += f"{key}: {value}\n"
    print(res)


@_input_error
def contacts_birthdays(args):
    birthdays = contacts.birthdays(args[0])
    print(birthdays)


@_input_error
def find_notes(args):
    key = args[0]

    # Code
    print(key)  # Test print | Clean after


@_input_error
def add_note(args):
    TITLE, text, *tags = args

    record = RecordNote()
    record.add_title(TITLE)
    record.add_note(text)
    record.add_tag(tags)
    notes.add_record(record)
    print("Note added")


@_input_error
def delete_note(args):
    TITLE = args[0]

    notes.delete(TITLE)
    print("Note deleted")


@_input_error
def change_note_title(args):
    TITLE, NEW_TITLE = args
    note = notes.find_note(TITLE)
    note.edit_title(NEW_TITLE)
    print("Note Title changed")


@_input_error
def change_note_text(args):
    TITLE, new_text = args

    note = notes.find_note(TITLE)
    note.edit_note(new_text)
    print("Note text changed")


@_input_error
def add_note_tags(args):
    TITLE, *tags = args

    note = notes.find_note(TITLE)
    note.add_tag(tags)
    print("Note added")


@_input_error
def delete_note_tag(args):
    TITLE, tag = args
    note = notes.find_note(TITLE)
    note.del_tag(tag)
    print("Note tag deleted")


@_input_error
def change_note_tag(args):
    TITLE, tag, new_tag = args
    note = notes.find_note(TITLE)
    note.edit_tag(tag, new_tag)
    print("Note tag changed")


@_input_error
def find_note_tag(args):
    tags = args
    res = notes.find_note_by_tag(tags)
    print(res)


@_input_error
def sort_note_tag(args):
    tags = args
    print(tags)


def main():
    contacts.read_from_file(FILENAME_CONTACTS)
    notes.read_csv_file(FILENAME_NOTES)

    msg = (
        Fore.LIGHTGREEN_EX
        + "\n==============================\n Welcome to the assistant bot!\n\nI will help you with your student activity.\n==============================\n"
    )
    print(msg)
    res = ""

    while True:
        # user_input = prompt(
        #     "Enter a command: ", completer=COMMANDS_TEST, complete_while_typing=False
        # )
        # Advanced version for Tab Autocomplete

        user_input = input(Fore.LIGHTBLUE_EX + "Enter a command: " + Fore.LIGHTWHITE_EX)
        # Basic version for Testing
        command, *args = _parse_input(user_input)

        if command in ["good bye", "close", "exit"]:
            res = close_bot()
            break
        elif command == "hello":
            res = helloBot()
        elif command == "help":
            res = helpBot()
        elif command == "add_contact":
            res = add_contact(args)
        elif command == "add_birthday":
            res = add_birthday(args)
        elif command == "delete_contact":
            res = delete_contact(args)
        elif command == "change_contact_phone":
            res = change_contact_phone(args)
        elif command == "find_contact":
            res = find_contact(args)
        elif command == "all_contacts":
            res = all_contacts()
        elif command == "add_address":
            res = add_address(args)
        elif command == "change_address":
            res = change_address(args)
        elif command == "add_email":
            res = add_email(args)
        elif command == "change_email":
            res = change_email(args)
        elif command == "find_notes":
            res = find_notes(args)
        elif command == "add_note":
            res = add_note(args)
        elif command == "delete_note":
            res = delete_note(args)
        elif command == "change_note_title":
            res = change_note_title(args)
        elif command == "change_note_text":
            res = change_note_text(args)
        elif command == "add_note_tags":
            res = add_note_tags(args)
        elif command == "delete_note_tag":
            res = delete_note_tag(args)
        elif command == "change_note_tag":
            res = change_note_tag(args)
        elif command == "find_note_tag":
            res = find_note_tag(args)
        elif command == "sort_note_tag":
            res = sort_note_tag(args)
        elif command == "contacts_birthdays":
            res = contacts_birthdays(args)
        else:
            res = Fore.RED + "Invalid command."
    print(res)


if __name__ == "__main__":
    main()

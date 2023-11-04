from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from components.notes.notes import RecordNote, NoteData
from components.contacts.contacts import RecordContact, AddressBook

from colorama import *

init(autoreset=True)


class Bot:
    def __init__(self):
        self.contacts = AddressBook()
        self.notes = NoteData()
        self.FILENAME_CONTACTS = "contacts.json"
        self.FILENAME_NOTES = "notes.csv"

        # COMMANDS LIST
        self.commands = {
            "hello": self.hello_bot,
            "close": self.close_bot,
            "good bye": self.close_bot,
            "exit": self.close_bot,
            "help": self.help_bot,
            "add_contact": self.add_contact,
            "add_address": self.add_address,
            "add_email": self.add_email,
            "add_birthday": self.add_birthday,
            "change_address": self.change_address,
            "change_email": self.change_email,
            "change_contact_phone": self.change_contact_phone,
            "delete_contact": self.delete_contact,
            "all_contacts": self.all_contacts,
            "find_contact": self.find_contact,
            "contacts_birthdays": self.contacts_birthdays,
            "all_notes": self.all_notes,
            "find_notes": self.find_notes,
            "add_note": self.add_note,
            "delete_note": self.delete_note,
            "change_note_title": self.change_note_title,
            "change_note_text": self.change_note_text,
            "add_note_tags": self.add_note_tags,
            "delete_note_tag": self.delete_note_tag,
            "change_note_tag": self.change_note_tag,
            "find_note_by_tag": self.find_note_by_tag,
            "sort_note_by_tags": self.sort_note_by_tags,
        }
        self.commands_help = [
            "hello",
            "close",
            "good bye",
            "exit",
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
            "all_notes",
            "find_notes TITLE || text || date",
            "add_note TITLE text #tags",
            "delete_note TITLE",
            "change_note_title TITLE NEW_TITLE",
            "change_note_text TITLE new_text",
            "add_note_tags TITLE #tags",
            "delete_note_tag TITLE #Tag",
            "change_note_tag TITLE #tag #new_tag",
            "find_note_by_tag #tags",
            "sort_note_by_tags",
        ]

    def run(self):
        self.contacts.read_from_file(self.FILENAME_CONTACTS)
        self.notes.read_csv_file(self.FILENAME_NOTES)

        COMMANDS_TEST = WordCompleter(
            self.commands.keys(),
            ignore_case=True,
        )

        msg = (
            Fore.LIGHTGREEN_EX
            + "\n==============================\n Welcome to the assistant bot!\n\nI will help you with your student activity.\n==============================\n"
        )
        print(msg)
        res = ""
        while True:
            # print(Fore.LIGHTBLUE_EX + "Enter a command: " + Fore.LIGHTWHITE_EX),
            user_input = prompt(
                "Enter a command: ",
                completer=COMMANDS_TEST,
                complete_while_typing=False,
            )
            command, *args = self._parse_input(user_input)
            if command in self.commands.keys() and command in [
                "good bye",
                "close",
                "exit",
            ]:
                res = self.commands[command](args)
                break
            elif command in self.commands.keys():
                res = self.commands[command](args)
            else:
                res = Fore.RED + "Invalid command."
            print(res)

    def _parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        if len(args) < 1 and cmd not in (
            "hello",
            "close",
            "close",
            "exit",
            "help",
            "all_contacts",
            "all_notes",
            "sort_note_by_tags",
        ):
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
            except Exception as e:
                return str(e)

        return inner

    def close_bot(self, args):
        self.contacts.save_to_file(self.FILENAME_CONTACTS)
        self.notes.write_csv_file(self.FILENAME_NOTES)
        return Fore.LIGHTYELLOW_EX + "Good bye!"

    def hello_bot(self, args):
        return Fore.LIGHTYELLOW_EX + "How can I help you?"

    def help_bot(self, args):
        res = ""
        for i in self.commands_help:
            res += f"{i}\n"
        return res

    @_input_error
    def add_contact(self, args):
        name, phone = args

        record = RecordContact(name)
        record.add_phone(phone)
        self.contacts.add_record(record)
        return "Contact added."

    @_input_error
    def change_contact_phone(self, args):
        name, phone = args
        contact = self.contacts.find(name)
        res = contact.edit_phone(phone)
        return res

    @_input_error
    def delete_contact(self, args):
        name = args[0]
        contact = self.notes.find_note(name)
        contact.delete_contact(name)
        return "Contact deleted"

    @_input_error
    def find_contact(self, args):
        name = args[0]
        found_contacts = self.contacts.search_contacts(name)
        if found_contacts:
            for contact in found_contacts:
                return contact
        else:
            return Fore.LIGHTMAGENTA_EX + "No contacts found."

    @_input_error
    def add_address(self, args):
        name, address = args
        contact = self.contacts.find(name)
        contact.add_address(address)
        return "Contact updated."

    @_input_error
    def change_address(self, args):
        name, address = args
        contact = self.contacts.find(name)
        res = contact.edit_address(address)
        return res

    @_input_error
    def add_email(self, args):
        name, email = args

        contact = self.contacts.find(name)
        contact.add_email(email)

        return "Email updated."

    @_input_error
    def add_birthday(self, args):
        name, birthday = args
        self.contacts.add_birthday(name, birthday)

    @_input_error
    def change_email(self, args):
        name, email = args
        contact = self.contacts.find(name)
        res = contact.edit_email(email)
        return res

    def all_contacts(self, args):
        res = Fore.MAGENTA + "\nAll Contacts:\n" + Fore.WHITE
        for key, value in self.contacts.items():
            res += f"{key}: {value}\n"
        return res

    @_input_error
    def contacts_birthdays(self, args):
        birthdays = self.contacts.birthdays(args[0])
        return birthdays

    @_input_error
    def all_notes(self, args):
        res = list(self.notes.data.items())
        if isinstance(res, list) and not None:
            for r in res:
                return r
        else:
            return res

    @_input_error
    def find_notes(self, args):
        key = " ".join(args)
        found_notes = self.notes.find_note(key)
        if isinstance(found_notes, list):
            for f in found_notes:
                return f
        else:
            return found_notes

    @_input_error
    def add_note(self, args):
        TITLE, text, *tags = args

        record = RecordNote()
        record.add_title(TITLE)
        record.add_note(text)
        record.add_tag(tags)
        self.notes.add_record(record)
        return record

    @_input_error
    def delete_note(self, args):
        TITLE = args[0]
        note = self.notes.find_note(TITLE)
        self.notes.delete(TITLE)
        message = str(note)
        message += "Note deleted"
        return message

    @_input_error
    def change_note_title(self, args):
        TITLE, NEW_TITLE = args
        note = self.notes.find_note(TITLE)
        note.edit_title(NEW_TITLE)
        return "Note Title changed"

    @_input_error
    def change_note_text(self, args):
        TITLE, new_text = args

        note = self.notes.find_note(TITLE)
        note.edit_note(new_text)
        message = str(note)
        message += "Note text changed"
        return message

    @_input_error
    def add_note_tags(self, args):
        TITLE, *tags = args

        note = self.notes.find_note(TITLE)
        note.add_tag(tags)
        t = " ".join(tags)
        return f"Note tag: {t} added"

    @_input_error
    def delete_note_tag(self, args):
        TITLE, tag = args
        note = self.notes.find_note(TITLE)
        note.del_tag(tag)
        return f"Note tag: {tag} deleted"

    @_input_error
    def change_note_tag(self, args):
        TITLE, tag, new_tag = args
        note = self.notes.find_note(TITLE)
        note.edit_tag(tag, new_tag)
        message = str(note)
        message += "Note tag changed"
        return message

    @_input_error
    def find_note_by_tag(self, args):
        tag = " ".join(args)
        res = self.notes.find_note_by_tag(tag)
        if isinstance(res, list):
            for r in res:
                return r
        else:
            return res

    @_input_error
    def sort_note_by_tags(self):
        res = self.notes.sort_note_by_tag_amount()
        if isinstance(res, list):
            for r in res:
                return r
        else:
            return res


if __name__ == "__main__":
    bot = Bot()
    bot.run()

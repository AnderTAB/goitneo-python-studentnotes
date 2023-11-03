# goitneo-student_notes

### Командний проект команди "2Left".

# Концепт:

Додаток для збереження контактів та ведення нотаток студентами. Має спростити повсякденне життя та позбавити необхідності вести паперовий записник.

# Пакети:

py -m pip install prompt_toolkit
py -m pip install colorama

# Функціонал:

При натисканні "Tab" ви можете побачити список всіх команд, а також, після введення частини команди і натискання "Tab", можете побачити в консолі найближчі відповідності.

# Команди:

"hello" - команда запускає бота та вітає користувача.
"close" - Використовуйте цю команду для закриття бота та завершення сеансу.
"good bye" - Використовуйте цю команду для закриття бота та завершення сеансу.
"exit" - Використовуйте цю команду для закриття бота та завершення сеансу.
"help" - Виводить доступні команди та короткий опис їх функціоналу.
"add_contact name phone" - Ця команда дозволяє додати новий контакт до вашого списку контактів з ім'ям та номером телефону.
"add_address name address" - Використовуйте цю команду для додавання адреси до існуючого контакту за ім'ям.
"add_email name email" - Додає нову електронну пошту до контакту за іменем.
"add_birthday name birthday(DD.MM.YYYY)" - Дозволяє додати день народження до контакту за іменем.
"change_address name new_address" - Змінює існуючу адресу контакту за іменем на нову.
"change_email name new_email" - Змінює існуючий email контакту за іменем на новий.
"change_contact_phone name phone" - Змінює номер телефону існуючого контакту за іменем.
"delete_contact name" - Видаляє контакт зі списку за іменем.
"all_contacts" - Показує список всіх контактів.
"find_contact name || address || phone || email || birthday(DD.MM.YYYY)" - Знаходить контакт за ім'ям, адресою, номером телефону, email або днем народження.
"contacts_birthdays days(int)" - Показує дні народження контактів, які відзначаються у вказану кількість днів в майбутньому.
"all_notes" - Показує список всіх нотаток.
"find_note TITLE || text || date" - Пошук нотаток за назвою, текстом або датою створення.
"add_note TITLE text #tags" - Додайте нову нотатку з заголовком, текстом і власними тегами.
"delete_note TITLE" - Видаляє нотатку за назвою.
"change_note_title TITLE NEW_TITLE" - Змінює заголовок існуючої нотатки.
"change_note_text TITLE new_text" - Змінює текст існуючої нотатки.
"add_note_tags TITLE #tags" - Додає теги до існуючої нотатки.
"delete_note_tag TITLE #Tag" - Видаляє тег з існуючої нотатки за назвою.
"change_note_tag TITLE #tag #new_tag" - Змінює тег в існуючій нотатці.
"find_note_tag #tags" - Знаходить нотатки за заданими тегами.
"sort_note_tags - Сортує нотатки за тегами.

# MIT License

Copyright (c) 2023 "2Left"

Дозволяється безоплатно кожному отримувати копію цього програмного забезпечення та відповідну документацію файлів (далі - "Програмне забезпечення"), щоб використовувати в Програмному забезпеченні без обмежень, включаючи, без обмежень, право використовувати, копіювати, змінювати, об'єднувати, публікувати, розповсюджувати, субліцензувати та/або продавати копії Програмного забезпечення, та дозволяє особам, які отримали Програмне забезпечення, це робити, за наступними умовами:

Вищевказана публікація авторського права та ця дозвільна заява повинні бути включені в усі копії або значущі частини Програмного забезпечення.

Програмне забезпечення надається "як є", без будь-яких гарантій, які, включаючи, без обмежень, гарантії на придатність для продажу, придатність для конкретної мети та відсутність порушень. Автори чи правовласники не несуть відповідальність за будь-яку пряму, індиректну, випадкову, особливу, екземплярну чи збиткову відповідальність, якщо така відповідальність несе збитки у зв'язку із використанням або невикористанням Програмного забезпечення або іншого виду взаємодії із Програмним забезпеченням.

# Автори:

Yehor Osipov; Yana Mudruk; Kostiantyn Romanchuk; Titov Andrii

---

# goitneo-student_notes

### Team project "2Left".

#Concept:
An application for storing contacts and taking notes by students. It aims to simplify everyday life and eliminate the need for a paper notebook.

# Packages:

py -m pip install prompt_toolkit
py -m pip install colorama

# Functionality:

Pressing "Tab" allows you to see a list of all commands, and after entering a part of the command and pressing "Tab," you can see the closest matches in the console.

# Commands:

"hello" - the command launches the bot and greets the user.
"close" - Use this command to close the bot and end the session.
"good bye" - Use this command to close the bot and end the session.
"exit" - Use this command to close the bot and end the session.
"help" - Displays available commands and a brief description of their functionality.
"add_contact name phone" - This command allows you to add a new contact to your list with a name and phone number.
"add_address name address" - Use this command to add an address to an existing contact by name.
"add_email name email" - Adds a new email to a contact by name.
"add_birthday name birthday(DD.MM.YYYY)" - Allows you to add a birthday to a contact by name.
"change_address name new_address" - Changes the existing address of a contact by name to a new one.
"change_email name new_email" - Changes the existing email of a contact by name to a new one.
"change_contact_phone name phone" - Changes the phone number of an existing contact by name.
"delete_contact name" - Deletes a contact from the list by name.
"all_contacts" - Shows a list of all contacts.
"find_contact name || address || phone || email || birthday(DD.MM.YYYY)" - Finds a contact by name, address, phone number, email, or birthday.
"contacts_birthdays days(int)" - Shows the birthdays of contacts that occur within the specified number of days in the future.
"all_notes" - Shows a list of all notes.
"find_notes TITLE || text || date" - Search for notes by title, text, or creation date.
"add_note TITLE text #tags" - Add a new note with a title, text, and custom tags.
"delete_note TITLE" - Deletes a note by title.
"change_note_title TITLE NEW_TITLE" - Changes the title of an existing note.
"change_note_text TITLE new_text" - Changes the text of an existing note.
"add_note_tags TITLE tags" - Adds tags to an existing note.
"delete_note_tag TITLE #Tag" - Removes a tag from an existing note by title.
"change_note_tag TITLE #tag #new_tag" - Changes a tag in an existing note.
"find_note_tag #tags" - Finds notes with specified tags.
"sort_note_tags" - Sorts notes by specified tags.

# MIT License

Copyright (c) 2023 "2Left"

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The authors or copyright holders shall not be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

# Authors:

Yehor Osipov; Yana Mudruk; Kostiantyn Romanchuk; Titov Andrii

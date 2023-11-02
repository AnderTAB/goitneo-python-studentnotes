import subprocess
import os

# Список команд для выполнения
commands = [
    "hello",
    "help",
    "add_contact Dave1 1234567890",
    "add_address",
    "add_address Dave1 Baker.str",
    "add_address Dave0 Baker.str",
    "add_address Dave1",
    "add_email",
    "add_email Dave1 emaildada@gmail.com",
    "add_email Dave0 emaildada@gmail.com",
    "add_email Dave1",
    "add_birthday",
    "add_birthday Dave1 12.06.1996",
    "add_birthday Dave0 12.06.1996",
    "add_birthday Dave1 12-06-1996",
    "add_birthday Dave1",
    "change_address",
    "change_address Dave1 Baker12.str",
    "change_address Dave0 Baker12.str",
    "change_address Dave1",
    "change_email",
    "change_email Dave1 emailNEWdada@gmail.com",
    "change_email Dave0 emailNEWdada@gmail.com",
    "change_email Dave1 emailNEWdada&gmail.com",
    "change_email Dave1",
    "add_contact DaveD 1234567890",
    "add_address DaveD Baker.str",
    "add_email DaveD emaildada@gmail.com",
    "add_birthday DaveD 12-6-1996",
    "add_contact DaveG 1234567890",
    "add_address DaveG Baker.str",
    "add_email DaveG emaildada@gmail.com",
    "add_birthday DaveG 12.6.1996",
    "add_contact DaveP 123",
    "add_address DaveP Baker.str",
    "add_email DaveP emaildada@gmail.com",
    "add_birthday DaveP 12.6.1996",
    "add_contact Dave",
    "add_address Dave Baker.str",
    "add_contact Dave00 1234567890",
    "add_address Dave00 Baker.str",
    "add_contact Dave01 1234567890",
    "add_address Dave01 Baker.str",
    "add_email Dave01 emaildada@gmail.com",
    "add_birthday Dave01 12.6.1996",
    "add_contact Dave2 1234567890",
    "add_address Dave2 Baker.str",
    "add_email Dave2 emaildada@gmail.com",
    "add_birthday Dave2 4.11.1996",
    "add_contact Dave3 1234567890",
    "add_address Dave3 Baker.str",
    "add_email Dave3 emaildada@gmail.com",
    "add_birthday Dave3 5.6.1996",
    "add_contact Dave4 1234567890",
    "add_address Dave4 Baker.str",
    "add_email Dave4 emaildada@gmail.com",
    "add_birthday Dave4 5.6.1996",
    "add_contact Dave5 1234567890",
    "add_address Dave5 Baker.str",
    "add_email Dave5 emaildada@gmail.com",
    "add_birthday Dave5 6.6.1996",
    "add_contact Dave6 1234567890",
    "add_address Dave6 Baker.str",
    "add_email Dave6 emaildada@gmail.com",
    "add_birthday Dave6 7.6.1996",
    "add_contact Dave7 1234567890",
    "add_address Dave7 Baker.str",
    "add_email Dave7 emaildada@gmail.com",
    "add_birthday Dave7 8.6.1996",
    "add_contact Dave8 1234567890",
    "add_address Dave8 Baker.str",
    "add_email Dave8 emaildada@gmail.com",
    "add_birthday Dave8 8.6.1996",
    "add_contact Dave9 1234567890",
    "add_address Dave9 Baker.str",
    "add_email Dave9 emaildada@gmail.com",
    "add_birthday Dave9 8.6.1996",
    "add_contact Dave10 1234567890",
    "add_address Dave10 Baker.str",
    "add_email Dave10 emaildada@gmail.com",
    "add_birthday Dave10 9.6.1996",
    "add_contact Dave11 1234567890",
    "add_address Dave11 Baker.str",
    "add_email Dave11 emaildada@gmail.com",
    "add_birthday Dave11 10.6.1996",
    "change_contact_phone",
    "change_contact_phone Dave4 1234567890",
    "change_contact_phone Dave4 0987654321",
    "change_contact_phone Dave4 123",
    "change_contact_phone Dave4",
    "change_contact Carl 1234567890",
    "delete_contact",
    "delete_contact Dave9",
    "delete_contact DaveXXX",
    "all_contacts",
]

file = os.path.abspath(f"src/bot.py")
# Запуск бота и передача команд
bot_process = subprocess.Popen(
    ["python", file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
)

for command in commands:
    bot_process.stdin.write(command + "\n")
    bot_process.stdin.flush()

# Завершение взаимодействия с ботом
bot_process.stdin.write("close\n")
bot_process.stdin.flush()

# Получение вывода бота
output, _ = bot_process.communicate()

print(output)

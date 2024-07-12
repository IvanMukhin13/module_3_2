def send_email(massage, recipient, sender='university.help@gmail.com'):  # recipient - получатель, sender - отправитель
    at_domen = ('.com', '.ru', '.net')
    if '@' not in recipient or '@' not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif not recipient.endswith(at_domen) or not sender.endswith(at_domen):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАРДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

""""
Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
Нельзя отправить письмо самому себе!
"""






# string_ = 'vasyok1337@gmail.com'
# string_1 = 'loyalty26@yande.ru.net'
# at = '@'
# domen_first_level = ['.com', '.ru', '.net']
#
# for word in domen_first_level:
#     if any(word in string_ for word in string_):
#         print(True)
#     else:
#         print(False)



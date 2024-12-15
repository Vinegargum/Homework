#Рассылка писем
def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if '@' not in recipient and sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif '.com' not in recipient and '.ru' not in recipient and '.net' not in recipient:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif '.com' not in sender and '.ru' not in sender and '.net' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

send_email('Здравствуйте! Мы ваши соседи снизу. Вы нас затопили.', 'waterfall.mail')
send_email('Сделайте домашку уже наконец!', 'hello.python@gmail.net')
send_email('Объявляю внеплановый отпуск!', 'university.help@gmail.com')
send_email('Напишите мне на ватсап, пж', 'student_1@mail.ru', 'teacher_1@gmail.com' )

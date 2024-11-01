y = '.com', '.ru', '.net', '@'
def send_email(message, recipient, sender = "university.help@gmail.com"):
    for i in range(1):
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
            break
        for j in range(len(y)):
            if recipient.__contains__(y[j]) or sender.__contains__(y[j]):
                if sender != "university.help@gmail.com":
                    print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ', recipient)
                    break
                print('Письмо успешно отправлено с адреса ', sender, 'на адрес ', recipient)
                break
            else:
                print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
                break
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
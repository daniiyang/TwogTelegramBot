import socket
import time
import socks
import telebot

import config

# инициализация бота и настройка носков. без носков не работает
ip = '127.0.0.1'
port = 9150
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
socket.socket = socks.socksocket

bot = telebot.TeleBot(token=config.TOKEN, threaded=False)

# инициализация всех глобальных переменных
order_lot = 0
order_application = 0

lot_1 = ' '
lot_2 = ' '
lot_3 = ' '
lot_4 = ' '
lot_5 = ' '
lot_6 = ' '
lot_7 = ' '
lot_8 = ' '
lot_9 = ' '
lot_10 = ' '

global USER_MESSAGE_CONTENT_TYPE
global CHAT_ID
global USER_ID
global USER_NAME
global USER_USERNAME
global USER_MASSAGE_TEXT
global USER_MESSAGE_ID


# создаем правильно оформленные сообщения пользователя
def formatting_user_message(user_message):
    # создание данных о пользователе и чате
    global USER_MESSAGE_CONTENT_TYPE
    global CHAT_ID
    global USER_ID
    global USER_NAME
    global USER_USERNAME
    global USER_MASSAGE_TEXT
    global USER_MESSAGE_ID

    USER_MESSAGE_CONTENT_TYPE = user_message.content_type
    CHAT_ID = user_message.chat.id
    USER_ID = user_message.from_user.id
    USER_USERNAME = user_message.from_user.username
    USER_MASSAGE_TEXT = user_message.text
    USER_MESSAGE_ID = user_message.message_id

    # фамилия бывает не указана, но если она есть, то это важно и ее нужно правильно вывести
    if user_message.from_user.last_name is None:
        USER_NAME = user_message.from_user.first_name
    else:
        USER_NAME = user_message.from_user.first_name + ' ' + user_message.from_user.last_name

    # еперь оформляем репорт
    global formatted_message
    global formatted_order

    formatted_message = """
    //content_type: {}
    chat_id: {}

    user_id: {}
    name: {} 
    username: {}

    message: {}""".format(USER_MESSAGE_CONTENT_TYPE,
                          CHAT_ID,
                          USER_ID,
                          USER_NAME,
                          USER_USERNAME,
                          USER_MASSAGE_TEXT)


# отправляем админам репорты по приходящим пользователям и их действиям
def reports_for_admins():
    if USER_MASSAGE_TEXT == '/start':
        bot.send_message(523011246, 'User {} ({}) joined the chatroom {}.'.format(USER_USERNAME, USER_NAME, CHAT_ID))
    elif USER_MASSAGE_TEXT == 'Заказать мерч 🔥':
        bot.send_message(523011246,
                         'User {} ({}) from {} gets to know the merch list.'.format(USER_USERNAME, USER_NAME, CHAT_ID))
    elif USER_MASSAGE_TEXT == 'Сервисы 💅🏻':
        bot.send_message(523011246,
                         'User {} ({}) from {} gets to know the list of services.'.format(USER_USERNAME, USER_NAME,
                                                                                          CHAT_ID))
    elif USER_MASSAGE_TEXT == 'Донат 🥰':
        bot.send_message(523011246,
                         'User {} ({}) from {} may want to make a donation.'.format(USER_USERNAME, USER_NAME, CHAT_ID))
    elif USER_MASSAGE_TEXT == 'Связь 📧':
        bot.send_message(523011246, 'User {} ({}) from {} meets the links.'.format(USER_USERNAME, USER_NAME, CHAT_ID))
    else:
        bot.send_message(523011246, 'User {} ({}) from {} said: "{}".'.format(USER_USERNAME, USER_NAME, CHAT_ID,
                                                                              USER_MASSAGE_TEXT))


# отправляем пользователям инструкцию об оплате админам репорты по полученным заказам
def sending_order_request(order_code):
    global formatted_order

    back_to_donate_list_button = telebot.types.InlineKeyboardMarkup()
    butt_back_to_donate_list = back_to_donate_list_button.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_donate_list'))

    if order_code == 1.1:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")
    elif order_code == 1.2:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")
    elif order_code == 1.3:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")
    elif order_code == 1.4:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")
    elif order_code == 1.5:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")
    elif order_code == 1.6:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")
    elif order_code == 1.7:
        bot.send_message(CHAT_ID, """Отправь в переводе ссылку на свою страницу в ВК и Код, чтобы я знал, по какому это делу происходит. Пожелание передам лично в руки или вышлю в месседжер - как захочешь. 
        Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:*""" % order_code, reply_markup=back_to_donate_list_button, parse_mode="Markdown")

    back_to_service_list_button = telebot.types.InlineKeyboardMarkup()
    butt_back_to_service_list = back_to_service_list_button.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_service_list'))

    if order_code == 2.1:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания.
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_service_list_button, parse_mode="Markdown")
    elif order_code == 2.2:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания.
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_service_list_button, parse_mode="Markdown")
    elif order_code == 2.3:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания.
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_service_list_button, parse_mode="Markdown")
    elif order_code == 2.4:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания.
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_service_list_button, parse_mode="Markdown")

    back_to_shop_list_button = telebot.types.InlineKeyboardMarkup()
    back_to_shop_list = back_to_shop_list_button.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_shop_list'))

    if order_code == 3.1:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
Еще раз спасибо~✨ 

*Код:* %s

*QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif order_code == 3.2:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
    Еще раз спасибо~✨ 

    *Код:* %s

    *QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif order_code == 3.3:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
    Еще раз спасибо~✨ 

    *Код:* %s

    *QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif order_code == 3.4:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
    Еще раз спасибо~✨ 

    *Код:* %s

    *QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif order_code == 3.5:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
    Еще раз спасибо~✨ 

    *Код:* %s

    *QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif order_code == 3.6:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
    Еще раз спасибо~✨ 

    *Код:* %s

    *QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif order_code == 3.7:
        bot.send_message(CHAT_ID, """При оплате отправь нам Код и ссылку на ВК, а также все нюансы и пожелания. Заказ передадим лично, в удобное время.
    Еще раз спасибо~✨ 

    *Код:* %s

    *QIWI, Сбер:* 89886697509""" % order_code, reply_markup=back_to_shop_list_button, parse_mode="Markdown")

    formatted_order = """
chat_id: {}  
user_id: {}
name: {} 
username: {}

lot: {}""".format(CHAT_ID,
                  USER_ID,
                  USER_NAME,
                  USER_USERNAME,
                  order_code)

    bot.send_message(523011246, formatted_order)


# сообщения только людям, которые обозначены
def welcome_special_user():
    if USER_USERNAME == 'Pass':
        bot.send_message(CHAT_ID, 'Pass')


def donate_list():
    try:
        global choose_donate_message
        global CHAT_ID

        donate_buttons = telebot.types.InlineKeyboardMarkup()

        butt_donate_gleb = donate_buttons.row(telebot.types.InlineKeyboardButton('❤ Глеб', callback_data='donate_gleb'))
        butt_donate_misha = donate_buttons.row(
            telebot.types.InlineKeyboardButton(' 🧡 Миша', callback_data='donate_misha'))
        butt_donate_roma = donate_buttons.row(
            telebot.types.InlineKeyboardButton(' 💛 Рома', callback_data='donate_roma'))
        butt_donate_lesha = donate_buttons.row(
            telebot.types.InlineKeyboardButton(' 💚 Леша', callback_data='donate_lesha'))
        butt_donate_vanya = donate_buttons.row(
            telebot.types.InlineKeyboardButton(' 💙 Ваня', callback_data='donate_vanya'))
        butt_donate_kirya = donate_buttons.row(
            telebot.types.InlineKeyboardButton(' 💜 Киря', callback_data='donate_kirya'))
        # butt_donate_dana = donate_buttons.row(telebot.types.InlineKeyboardButton(' 🤍 Дана', callback_data='donate_dana'))
        butt_donate_all = donate_buttons.row(
            telebot.types.InlineKeyboardButton(' Деритесь', callback_data='donate_all'))

        choose_donate_message = bot.send_message(CHAT_ID, 'Уву, хочешь сделать нам приятно?',
                                                 reply_markup=donate_buttons)
    except:
        pass


def services_list():
    try:
        global choose_service_message

        service_buttons = telebot.types.InlineKeyboardMarkup()

        butt_service = service_buttons.row(telebot.types.InlineKeyboardButton('Сигна', callback_data='service_lot_1'))
        butt_service = service_buttons.row(telebot.types.InlineKeyboardButton('Реклама', callback_data='service_lot_2'))
        butt_service = service_buttons.row(
            telebot.types.InlineKeyboardButton('Ноготки в стиле TWOG', callback_data='service_lot_3'))
        butt_service = service_buttons.row(telebot.types.InlineKeyboardButton('Опрос', callback_data='service_lot_4'))

        choose_service_message = bot.send_message(CHAT_ID, 'Нажми, чтобы глянуть описание товара 📜',
                                                  reply_markup=service_buttons)
    except:
        pass


def shop_list():
    try:
        global choose_shop_message

        price_list_buttons = telebot.types.InlineKeyboardMarkup()

        price_list_buttons.row(telebot.types.InlineKeyboardButton('Противодетные', callback_data='shop_lot_1'))
        price_list_buttons.row(telebot.types.InlineKeyboardButton('Suorin air TWOG plus', callback_data='shop_lot_2'))
        price_list_buttons.row(telebot.types.InlineKeyboardButton('Suorin air TWOG', callback_data='shop_lot_3'))
        price_list_buttons.row(telebot.types.InlineKeyboardButton('Наклейка TWOG', callback_data='shop_lot_4'))
        price_list_buttons.row(telebot.types.InlineKeyboardButton('Майка TWOG "Оп, было"', callback_data='shop_lot_5'))
        price_list_buttons.row(telebot.types.InlineKeyboardButton('Майка TWOG', callback_data='shop_lot_6'))
        price_list_buttons.row(telebot.types.InlineKeyboardButton('Значек TWOG', callback_data='shop_lot_7'))
        # price_list_buttons.row(telebot.types.InlineKeyboardButton('Лот 8', callback_data='shop_lot_8'))
        # price_list_buttons.row(telebot.types.InlineKeyboardButton('Лот 9', callback_data='shop_lot_9'))
        # price_list_buttons.row(telebot.types.InlineKeyboardButton('Лот 10', callback_data='shop_lot_10'))

        choose_shop_message = bot.send_message(CHAT_ID, 'Нажми, чтобы глянуть описание товара 📜',
                                               reply_markup=price_list_buttons)
    except:
        pass


@bot.callback_query_handler(func=lambda call: True)
def donate_shop_service_profiles(call):
    global order_code

    """ ПРОФИЛИ ДОНАТОВ """
    global choose_donate_message

    back_to_donate_list_button = telebot.types.InlineKeyboardMarkup()
    butt_buy_donate = back_to_donate_list_button.row(
        telebot.types.InlineKeyboardButton('Задонатить', callback_data='buy_donate'),
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_donate_list'))

    back_to_donate_list_button_1 = telebot.types.InlineKeyboardMarkup()
    butt_back_to_donate_list = back_to_donate_list_button_1.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_donate_list'))

    if call.data == 'donate_gleb':
        order_code = 1.1

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_test.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message_1 = bot.send_message(call.message.chat.id, """*Глеб Василевский - Отец TWOG*
        
Задонать мне соточку, и я напишу лучшее пожелание в твоей жизни ✨""", reply_markup=back_to_donate_list_button,
                                                   parse_mode="Markdown")
    elif call.data == 'donate_misha':
        order_code = 1.2

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_test.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message_1 = bot.send_message(call.message.chat.id, """*Михаил Кисилев - Администратор премиум класса*
        
Задонать мне соточку, и я напишу лучшее пожелание в твоей жизни ✨""", reply_markup=back_to_donate_list_button,
                                                   parse_mode="Markdown")
    elif call.data == 'donate_roma':
        order_code = 1.3

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_test.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message_1 = bot.send_message(call.message.chat.id, """*Рома Корчнев - Дизайн, организация мероприятий*
        
Задонать мне соточку, и я напишу лучшее пожелание в твоей жизни ✨""", reply_markup=back_to_donate_list_button,
                                                   parse_mode="Markdown")
    elif call.data == 'donate_lesha':
        order_code = 1.4

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_test.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message_1 = bot.send_message(call.message.chat.id, """*Алексей Архиреев - Оператор, фотограф, DJ*
        
Задонать мне соточку, и я напишу лучшее пожелание в твоей жизни ✨""", reply_markup=back_to_donate_list_button,
                                                   parse_mode="Markdown")
    elif call.data == 'donate_vanya':
        order_code = 1.5

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_test.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message_1 = bot.send_message(call.message.chat.id, """*Ваня Василов - Мажор*
        
Задонать мне соточку, и я напишу лучшее пожелание в твоей жизни ✨""", reply_markup=back_to_donate_list_button,
                                                   parse_mode="Markdown")
    elif call.data == 'donate_kirya':
        order_code = 1.6

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_test.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message_1 = bot.send_message(call.message.chat.id, """*Кирилл Шаршаков - Кэп*
        
Задонать мне соточку, и я напишу лучшее пожелание в твоей жизни ✨""", reply_markup=back_to_donate_list_button,
                                                   parse_mode="Markdown")
    elif call.data == 'donate_all':
        order_code = 1.7

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/donate_profile_img_all.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_donate_message = bot.send_message(call.message.chat.id,
                                                 """Так, значит? Донат будет поделен поровну, а пожелание напишет админ, выбранный ГСЧ.""",
                                                 reply_markup=back_to_donate_list_button)

    if call.data == 'back_to_donate_list':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        except:
            pass
        bot.delete_message(call.message.chat.id, call.message.message_id)
        donate_list()

    """ ПРОФИЛИ СЕРВИСОВ """
    global choose_service_message

    back_to_service_list_button = telebot.types.InlineKeyboardMarkup()
    butt_buy_service = back_to_service_list_button.row(
        telebot.types.InlineKeyboardButton('Купить', callback_data='buy_service'),
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_service_list'))

    back_to_service_list_button_1 = telebot.types.InlineKeyboardMarkup()
    butt_back_to_service_list_1 = back_to_service_list_button_1.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_service_list'))

    if call.data == 'service_lot_1':
        order_code = 2.1

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/services_profile_img_signa.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_service_message = bot.send_message(call.message.chat.id, """*Сигна 📸*

Сигна от любого нашего админа, с подписью и надписью (кому, от кого, пожелания и т.п.). Надпись может быть выбрана по вашему желанию.

*Цена: 20р*""",
                                                  reply_markup=back_to_service_list_button, parse_mode="Markdown")
    elif call.data == 'service_lot_2':
        order_code = 2.2

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/services_profile_img_reklama.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_service_message = bot.send_message(call.message.chat.id, """*Реклама 📢*

Реклама вашего сообщества/сайта/профиля/фирмы и др..

*Цена: 50р*""",
                                                  reply_markup=back_to_service_list_button, parse_mode="Markdown")
    elif call.data == 'service_lot_3':
        order_code = 2.3

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/services_profile_img_nogotochki.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_service_message = bot.send_message(call.message.chat.id, """*Ноготки в стиле TWOG 💅🏻*
        
Сделаем вам ноготочки в стиле TWOG быстро и недорого. Дизайн и технология нанесения постоянно совершенствуются.

*Цена: 50р*""", reply_markup=back_to_service_list_button, parse_mode="Markdown")
    elif call.data == 'service_lot_4':
        order_code = 2.4

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/services_profile_img_opros.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_service_message = bot.send_message(call.message.chat.id, """*Опрос в группе ВК 〽*

Мы выкладываем в группу составленный вами социальный опрос для вашей проектной работы, либо создания статистики (особенно полезно ученикам 8-10 классов).

*Цена: 5р*""",
                                                  reply_markup=back_to_service_list_button, parse_mode="Markdown")

    if call.data == 'back_to_service_list':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        except:
            pass
        bot.delete_message(call.message.chat.id, call.message.message_id)
        services_list()

    """ ПРОФИЛИ ТОВАРОВ ШОПА """
    global choose_shop_message

    back_to_shop_list_button = telebot.types.InlineKeyboardMarkup()
    back_to_shop_list = back_to_shop_list_button.row(
        telebot.types.InlineKeyboardButton('Купить', callback_data='buy_shop'),
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_shop_list'))

    back_to_shop_list_button_1 = telebot.types.InlineKeyboardMarkup()
    back_to_shop_list_1 = back_to_shop_list_button_1.row(
        telebot.types.InlineKeyboardButton('Назад', callback_data='back_to_shop_list'))

    if call.data == 'shop_lot_1':
        order_code = 3.1

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_protivodetnoe.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Противодетные 👨‍👧*
        
Гандон, чтобы у тебя не появился гандон.

*Цена: 65р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif call.data == 'shop_lot_2':
        order_code = 3.2

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_suorinplus.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Suorin air TWOG plus 💨*

Улучшенная версия Sourin air TWOG. С куда лучшими и характеристиками, и набором.

*Цена: 2500р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif call.data == 'shop_lot_3':
        order_code = 3.3

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_suorin.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Suorin air TWOG 💨*

Стильный минивейп с любимым логотипом. Отличный способ уйти от сигарет (особая комплектация набора).

*Цена: 2000р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif call.data == 'shop_lot_4':
        order_code = 3.4

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_sticker.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Наклейка TWOG 🔳*

Фирменная наклейка TWOG (3,3 * 2,2)

*Цена: 10р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif call.data == 'shop_lot_5':
        order_code = 3.5

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_maykaop.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Майка TWOG "Оп, было" 👌🏿*

Красивая майка, которая отлично дополнит ваш гардероб. Также можно бить людей, смотрящих вам в спину)
(все майки делаются на заказ!)

*Цена: 600р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif call.data == 'shop_lot_6':
        order_code = 3.6

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_mayka.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Майка TWOG 👕*

Белая майка с надписью TWOG. Вы можете выбрать любой классический шрифт, поддерживаемый системами Linux и Windows, а также положение, размер и другие свойства надписи.

*Цена: 500р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")
    elif call.data == 'shop_lot_7':
        order_code = 3.7

        bot.delete_message(call.message.chat.id, call.message.message_id)

        photo = open('images/shop_profile_img_znachek.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

        choose_shop_message = bot.send_message(call.message.chat.id, """*Значек TWOG 🔘*

Значок с иголкой, белый, с чёрной надписью. Вы можете выбрать любой шрифт, поддерживаемый системами Windows и Linux и размер надписи. По вашему желанию можно изменить положение и свойства текста.

*Цена: 25р*""", reply_markup=back_to_shop_list_button, parse_mode="Markdown")

    if call.data == 'back_to_shop_list':
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        except:
            pass
        bot.delete_message(call.message.chat.id, call.message.message_id)
        shop_list()

    """ ОФОРМЛЕНИЕ ЗАЯВКИ """
    global formatted_order

    if call.data == 'buy_donate':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id)

        sending_order_request(order_code)

    elif call.data == 'buy_service':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id)

        sending_order_request(order_code)

    elif call.data == 'buy_shop':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id)

        sending_order_request(order_code)


# начало работы юзера с ботом
@bot.message_handler(commands=['start'])
def welcome_user(user_message):
    formatting_user_message(user_message)
    welcome_special_user()

    menu_buttons = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu_buttons.row(telebot.types.InlineKeyboardButton('Заказать мерч 🔥'))
    menu_buttons.row(telebot.types.InlineKeyboardButton('Сервисы 💅🏻'))
    menu_buttons.row(telebot.types.InlineKeyboardButton('Донат 🥰'))
    menu_buttons.row(telebot.types.InlineKeyboardButton('Связь 📧'))

    bot.send_sticker(CHAT_ID, 'CAACAgIAAxkBAAIfx141HRSJI_hf_wOg2xGLeavtU38sAALTAgAC8-O-C4FE99F2LOuxGAQ')
    bot.send_message(CHAT_ID, 'Хей, друг! Здесь ты можешь заказать наш мерч, мальчика на ночь или просто '
                              'задонатить и получить милое пожелание 💌', reply_markup=menu_buttons)

    reports_for_admins()


@bot.message_handler(content_types=['text'])
def keyboard_commands(user_message):
    formatting_user_message(user_message)

    global USER_MASSAGE_TEXT

    if USER_MASSAGE_TEXT.lower() == 'заказать мерч 🔥':
        USER_MASSAGE_TEXT = 'Заказать мерч 🔥'
        shop_list()
        reports_for_admins()

    elif USER_MASSAGE_TEXT.lower() == 'сервисы 💅🏻':
        USER_MASSAGE_TEXT = 'Сервисы 💅🏻'

        services_list()
        reports_for_admins()

    elif USER_MASSAGE_TEXT.lower() == 'донат 🥰':
        USER_MASSAGE_TEXT = 'Донат 🥰'

        donate_list()
        reports_for_admins()

    elif USER_MASSAGE_TEXT.lower() == 'связь 📧':
        USER_MASSAGE_TEXT = 'Связь 📧'

        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                'По всем вопросам сюда', url='telegram.me/diidanart'))
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                'Паблик в ВК', url='https://vk.com/gleblans'))
        bot.send_message(CHAT_ID, "Ссылочки:", reply_markup=keyboard)

        reports_for_admins()
    else:
        reports_for_admins()


def alerts(user_message):
    bot.send_message(CHAT_ID, 'Хэй, не тупи слишком долго, лоты могут исчезнуть в '
                              'любую минуту, уж такое это непредсказуемое дело!')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(5)

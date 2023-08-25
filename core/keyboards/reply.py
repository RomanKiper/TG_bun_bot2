from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard_second_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Рекламодателям'
        )
    ],
    [
        KeyboardButton(
            text='Частным лицам'
        )
    ],
    [
        KeyboardButton(
            text='Работникам компании'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Сделайте выбор 👇", selective=True)


loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='отправить геолокацию',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Отправить свой контакт',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType()      #type="quiz" пользователь может создать викторину
        )                                              #type="regular" пользователь может создать опрос с несколькими вариантами ответов
    ]
],resize_keyboard=True, one_time_keyboard=False, input_field_placeholder="Отправь локацию, номер телефона, или создай викторину/опрос")
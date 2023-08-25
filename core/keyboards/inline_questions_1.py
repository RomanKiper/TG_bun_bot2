from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_questions_private_person = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Как купить промокод",
            callback_data='howtobuy'
        )
    ],
    [
        InlineKeyboardButton(
            text="Как воспользоваться промокодом",
            callback_data='howtouse'
        )
    ],
    [
        InlineKeyboardButton(
            text="Какой срок действия промокода",
            callback_data='whatisterms'
        )
    ],
    [
        InlineKeyboardButton(
            text="Можно ли дарить промокоды",
            callback_data='canipresent'
        )
    ],
    [
        InlineKeyboardButton(
            text="Можно ли купить нескольк промокодов",
            callback_data='can_ibymore'
        )
    ],
    [
        InlineKeyboardButton(
            text="Сколько стоит промкод",
            callback_data='howmuch'
        )
    ],
    [
        InlineKeyboardButton(
            text="Можно ли вернуть промокод",
            callback_data='canireturn'
        )
    ],
    [
        InlineKeyboardButton(
            text="Еще один вопрос?",
            callback_data='onemore'
        )
    ],
    [
        InlineKeyboardButton(
            text="Вернуться в меню",
            callback_data="back_to_private_menu"
        )
    ],
])
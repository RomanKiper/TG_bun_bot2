from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_menu_private_person = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Часто задаваемые вопросы",
            callback_data='faq1'
        )
    ],
    [
        InlineKeyboardButton(
            text="Способы связаться со slivki.by",
            callback_data="how_to_contact"
        )
    ],
    [
        InlineKeyboardButton(
            text="Скачать приложение slivki.by",
            callback_data="download_app"
        )
    ],
    [
        InlineKeyboardButton(
            text="Веруться в главное меню",
            callback_data="back_to_main_menu"
        )
    ]
])

inline_second_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Частное лицо",
            callback_data='private_person'
        )
    ],
    [
        InlineKeyboardButton(
            text="Рекламодатель",
            callback_data="advertiser"
        )
    ],
    [
        InlineKeyboardButton(
            text="Работник компании",
            callback_data="company_employee",
        )
    ],
])

inline_list_media = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="slivki.by",
            url="https://www.slivki.by"
        )
    ],
    [
        InlineKeyboardButton(
            text="Telegram",
            url="https://t.me/slivki_by"
        )
    ],
    [
        InlineKeyboardButton(
            text="Instagram slivki.by",
            url="https://www.instagram.com/slivkiby/"
        )
    ],
    [
        InlineKeyboardButton(
            text="TikTok",
            url="https://www.tiktok.com/@slivkiby"
        )
    ]
])

inline_link_download_app = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Скачать приложение SLIVKI.BY",
            url="https://www.slivki.by/prilozhenie-skidok"
        )
    ]
])

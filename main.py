from aiogram import Bot, Dispatcher
from core.handlers.basic import get_start, get_photo, get_hello, open_second_menu, get_reply_keyboard_contact_location_quiz_regular
from core.handlers.basic import get_location, get_list_media
from aiogram.types import Message, ContentType
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_fake_contact
import asyncio
import logging
from core.settings import settings
from aiogram import F
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.handlers.basic import get_inline_menu_private_person, get_description_bot, reply_download_app
from core.handlers.callback import select_bat_second_menu, back_to_main_menu, inline_download_app, \
    get_inline_list_private_questions
import json


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(1006569664, text="Бот остановлен!")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s -[%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.startup.register(stop_bot)
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_reply_keyboard_contact_location_quiz_regular, Command(commands=['quiz', "run"]))
    dp.message.register(get_location, F.location)
    dp.message.register(get_hello, F.text == "Привет")
    dp.message.register(open_second_menu, Command(commands=['main_menu']))
    dp.message.register(get_list_media, Command(commands=['our_media']))
    dp.message.register(get_description_bot, Command(commands=['description_bot']))
    dp.message.register(reply_download_app, Command(commands=['download_app']))
    dp.callback_query.register(select_bat_second_menu, F.data.startswith("private_person"))
    dp.callback_query.register(back_to_main_menu, F.data.startswith("back_to_main_menu"))
    dp.callback_query.register(inline_download_app, F.data.startswith("download_app"))
    dp.callback_query.register(get_inline_list_private_questions, F.data.startswith("faq1"))

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())



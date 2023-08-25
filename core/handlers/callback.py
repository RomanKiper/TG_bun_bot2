from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards.inline import inline_menu_private_person
from core.keyboards.inline import inline_second_menu, inline_list_media, inline_link_download_app
from core.keyboards.inline_questions_1 import inline_questions_private_person


async def select_bat_second_menu(call: CallbackQuery, bot: Bot):
    await call.message.answer(text="Вы сделали выбор категориииии", reply_markup=inline_menu_private_person)


async def back_to_main_menu(call: CallbackQuery, bot: Bot):
    await call.message.answer(f"Выберите свою категорию.....!!!", reply_markup=inline_second_menu)


async def inline_download_app(call: CallbackQuery, bot: Bot):
    await call.message.answer(f"👇👇Перейди по ссылке👇👇", reply_markup=inline_link_download_app)



async def get_inline_list_private_questions(call: CallbackQuery, bot: Bot):
    await call.message.answer(text="Выберите вопрос", reply_markup=inline_questions_private_person)

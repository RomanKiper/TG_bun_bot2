import json

from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard_second_menu, loc_tel_poll_keyboard
from core.keyboards.inline import inline_menu_private_person, inline_second_menu, inline_list_media, inline_link_download_app
from aiogram.types import BotCommand, BotCommandScopeDefault


async def get_inline_menu_private_person(message: Message, bot: Bot):
    await message.answer(f"Выберите нужный пункт.......:",
                         reply_markup=inline_menu_private_person)


async def get_reply_keyboard_contact_location_quiz_regular(message: Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.first_name}. Рад тебя видеть!",
                         reply_markup=loc_tel_poll_keyboard)


async def get_location(message: Message, bot: Bot):
    await message.answer(f"Ты отправил локацию!\r\a"
                         f"{message.location.latitude}\r\n{message.location.longitude}")



async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}. Рад тебя видеть!")
    await message.answer(f"Привет {message.from_user.first_name}. Рад тебя видеть!")
    await message.reply(f"Привет {message.from_user.first_name}. Рад тебя видеть!")


async def get_photo(message, bot: Bot):
    await message.answer(f"Отлично! ты отправил картинку, я сохраню ее себе!")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, "photo.jpg")


async def get_hello(message: Message, bot: Bot):
    await message.answer(f"И тебе привет!")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)


async def open_second_menu(message: Message, bot: Bot):
    await message.answer(f"Выберите свою категорию.!", reply_markup=inline_second_menu)
    await message.delete()


async def get_list_media(message: Message, bot: Bot):
    await message.answer(f"Наши медиа!", reply_markup=inline_list_media)
    await message.delete()


async def get_description_bot(message: Message, bot: Bot):
    await message.answer(f"""BUN_bot является виртуальным помошником компаии slivki.by. Его задача - дать партнерам и клиентам
информацию о работе со сливками, ответить на стандартные вопросы! """)
    await message.delete()


async def reply_download_app(message: Message, bot: Bot):
    await message.answer(text="👇👇Перейди по ссылке👇👇", reply_markup=inline_link_download_app)
    await message.delete()

import os

from aiogram import Bot, Dispatcher, executor, types
from config import Token
import logging
from keyboards import *

# proxy_url = 'http://proxy.server:3128'

bot = Bot(token=Token)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)


async def set_start_command(bot: Bot, chat_id):
    return await bot.set_my_commands(
        commands=[
            types.BotCommand('start', 'restart bot'),
            types.BotCommand('help', 'info about bot'),
        ],
        scope=types.BotCommandScopeChat(chat_id),
        language_code='ru'
    )


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f' Привет, {message.from_user.full_name}, это бот про мои достижения в футболе ⚽\n'
                         f'выберите один из вариантов ниже 👇 ', reply_markup=start_kb)
    await set_start_command(bot, message.chat.id)


@dp.callback_query_handler(text='team')
async def team(call: types.CallbackQuery):
    # await call.message.delete()
    await call.message.edit_text('вы попали в раздел командных достижений\n'
                                 'выберите интересующий вас год', reply_markup=get_kbyears_team())


@dp.callback_query_handler(text='player')
async def player(call: types.CallbackQuery):
    # await call.message.delete()
    await call.message.edit_text('вы попали в раздел личных достижений\n'
                                 'выберите интересующий вас год', reply_markup=get_kbyears_pers())


@dp.callback_query_handler(text='Back')
async def back(call: types.CallbackQuery):
    await call.message.edit_text(f' Привет, {call.from_user.full_name}, это бот про мои достижения в футболе ⚽\n'
                                 f'выберите один из вариантов ниже 👇 ', reply_markup=start_kb)


@dp.callback_query_handler(text_startswith='teamyear')
async def teamyear(call: types.CallbackQuery):
    data = call.data
    await call.message.delete()
    working_directory = os.getcwd()
    if data == 'teamyear_2020':
        file_path = working_directory + '\\team_2020.jpg'
        file = open(file_path, 'rb')
        caption = 'Турнир Наше Будущее'
    elif data == 'teamyear_2021_1':
        file_path = working_directory + '\\team_2021.jpg'
        file = open(file_path, 'rb')
        caption = 'Чемпионат Клубная Лига'

    elif data == 'teamyear_2021_2':
        file_path = working_directory + '\\team_2021_2.jpg'
        file = open(file_path, 'rb')
        caption = 'Чемпионат ЕФЛ'


    elif data == 'teamyear_2022':
        file_path = working_directory + '\\team_2022.jpg'
        file = open(file_path, 'rb')
        caption = 'Чемпионат 3 Лиги '

    await call.message.answer_photo(photo=file, caption=caption, reply_markup=back_years)


@dp.callback_query_handler(text='back_teamyears')
async def back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('вы попали в раздел командных достижений\n'
                              'выберите интересующий вас год', reply_markup=get_kbyears_team())


@dp.callback_query_handler(text_startswith='persyear')
async def teamyear(call: types.CallbackQuery):
    data = call.data
    await call.message.delete()
    if data == 'persyear_2019':
        working_directory = os.getcwd()
        file_path = working_directory + '\\pers_2019.jpg'
        file = open(file_path, 'rb')
        caption = 'Лучший Игрок Команды в 2019'
    elif data == 'persyear_2020':
        working_directory = os.getcwd()
        file_path = working_directory + '\\pers_2020.jpg'
        file = open(file_path, 'rb')
        caption = 'Лучший Игрок Команды в 2020'

    elif data == 'persyear_2022':
        working_directory = os.getcwd()
        file_path = working_directory + '\\pers_2022.jpg'
        file = open(file_path, 'rb')
        caption = 'Лучший Игрок Команды На Турнире'

    elif data == 'persyear_2022_2':
        working_directory = os.getcwd()
        file_path = working_directory + '\\pers_2022_2.jpg'
        file = open(file_path, 'rb')
        caption = 'Лучший Игрок Команды Кубок Валентина Афонова'

    await call.message.answer_photo(photo=file, caption=caption, reply_markup=pers_years)


@dp.callback_query_handler(text='back_persyears')
async def back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('вы попали в раздел личных достижений\n'
                              'выберите интересующий вас год', reply_markup=get_kbyears_pers())


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply(f'you pressed command help {message.from_user.first_name} ')


@dp.message_handler(commands='menu')
async def home(message: types.Message):
    await message.reply(f'you pressed command menu {message.from_user.first_name} ')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f'you wrote {message.text}')
    await set_starting_commands(bot, message.chat.id)


async def on_startup(dp):
    await bot.send_message(5242177328, 'i am ready')


async def set_starting_commands(bot: Bot, chat_id: int):
    await bot.set_my_commands([
        types.BotCommand('start', 'bot restart'),
        types.BotCommand('help', 'info about bot'),
        types.BotCommand('menu', 'main page'),
    ], scope=types.BotCommandScopeChat(chat_id), language_code='ru')


executor.start_polling(dp, on_startup=on_startup)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup()# создание клавиатуры
command_btn = InlineKeyboardButton(text= 'командные', callback_data= 'team')# создание кнопки
personal_btn = InlineKeyboardButton(text= 'личные', callback_data= 'player')# создание кнопки
start_kb.add(command_btn, personal_btn)


def get_kbyears_team():
    buttons = [
        InlineKeyboardButton(text='2020', callback_data='teamyear_2020'),
        InlineKeyboardButton(text='2021 (1)', callback_data='teamyear_2021_1'),
        InlineKeyboardButton(text='2021 (2)', callback_data='teamyear_2021_2'),
        InlineKeyboardButton(text='2022', callback_data='teamyear_2022'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='Back'))
    return keyboard



def get_kbyears_pers():
    buttons = [
        InlineKeyboardButton(text='2019', callback_data='persyear_2019'),
        InlineKeyboardButton(text='2020', callback_data='persyear_2020'),
        InlineKeyboardButton(text='2022 (1)', callback_data='persyear_2022'),
        InlineKeyboardButton(text='2022 (2)', callback_data='persyear_2022_2'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    keyboard.add(InlineKeyboardButton(text='Назад', callback_data='Back'))
    return keyboard


back_years = InlineKeyboardMarkup().add(InlineKeyboardButton('Назад', callback_data='back_teamyears'))
pers_years = InlineKeyboardMarkup().add(InlineKeyboardButton('Назад', callback_data='back_persyears'))



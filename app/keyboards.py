from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database import get_usernames

register = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать регистрацию")]], resize_keyboard=True, input_field_placeholder="Начните регистрацию...")


admin_panel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Посмотреть данные", callback_data="check_data")],
                                                    [InlineKeyboardButton(text="Добавить данные", callback_data="add_data")]])


async def inline_users():
    users = get_usernames()
    keyboard = InlineKeyboardBuilder()
    for user in users:
        keyboard.add(InlineKeyboardButton(text=user[0], url="https://google.com")) # Dummy url
    return keyboard.adjust(2).as_markup()

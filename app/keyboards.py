from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database import get_usernames

register = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="📝Начать регистрацию")]], resize_keyboard=True, input_field_placeholder="Начните регистрацию...")


admin_panel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="👀Посмотреть данные", callback_data="check_data")],
                                                    [InlineKeyboardButton(text="✍️Добавить данные", callback_data="add_data")]])


return_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️Вернуться", callback_data="return")]])

async def users():
    users = get_usernames()
    keyboard = InlineKeyboardBuilder()
    for user in users:
        username = user[0]
        keyboard.add(InlineKeyboardButton(text=username, callback_data=f"user_{username}"))
    return keyboard.adjust(2).as_markup()
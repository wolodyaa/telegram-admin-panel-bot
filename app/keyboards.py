from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database import get_usernames

register = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="📝Начать регистрацию")]], resize_keyboard=True, input_field_placeholder="Начните регистрацию...")


admin_panel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="👀Посмотреть данные", callback_data="check_data")],
                                                    [InlineKeyboardButton(text="🗑Удалить данные", callback_data="delete_data")]])


return_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️Вернуться", callback_data="return")]])


confirm_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="confirm_yes"), InlineKeyboardButton(text="Нет", callback_data="confirm_no")]])


async def users(delete):
    if delete:
        prefix = "delete"
    else:
        prefix = "check"
    users = get_usernames()
    keyboard = InlineKeyboardBuilder()
    for user in users:
        username = user[0]
        if not username:
            continue
        keyboard.add(InlineKeyboardButton(text=username, callback_data=f"{prefix}_user_{username}"))
    return keyboard.adjust(2).as_markup()
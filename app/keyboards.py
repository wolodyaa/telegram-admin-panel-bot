from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

register = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать регистрацию")]], resize_keyboard=True, input_field_placeholder="Начните регистрацию...")


admin_panel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Посмотреть данные", callback_data="check_data")],
                                                    [InlineKeyboardButton(text="Добавить данные", callback_data="add_data")]])
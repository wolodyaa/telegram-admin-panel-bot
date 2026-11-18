from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from assets.config import ADMIN_ID

import app.keyboards as kb
import app.states as st
import app.database as db


router = Router()

@router.message(CommandStart())
async def cmdstart(message: Message):
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer("Привет! Нажимай кнопку снизу чтобы начать регистрацию.", reply_markup=kb.register)
    else:
        name = user_info
        await message.answer(f"Привет {name}!")


@router.message(F.text == "Начать регистрацию")
async def register_start(message: Message, state: FSMContext):
    user_info = db.get_reg_data(message.from_user.id)
    if not user_info:
        await message.answer("Введи своё имя.")
        await state.set_state(st.Register.waiting_name)
    else:
        name = user_info
        await message.answer(f"Ты уже зарегистрировался как: {name}.")


@router.message(st.Register.waiting_name)
async def register_name(message: Message, state: FSMContext):
    text = message.text.strip()
    await message.answer("Введи свою фамилию.")
    await state.update_data(name=text)
    await state.set_state(st.Register.waiting_surname)


@router.message(st.Register.waiting_surname)
async def register_surname(message: Message, state: FSMContext):
    surname = message.text.strip()
    data = await state.get_data()
    await message.answer("Ты успешно зарегистрировался!\n"
                         "Твои данные:\n"
                         f"Имя: {data['name']}\n"
                         f"Фамилия: {surname}")

    db.register(message.from_user.id, message.from_user.username, data['name'], surname)

    await state.clear()


@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Вы вошли в админскую панель.", reply_markup=kb.admin_panel)
    else:
        await message.answer("🚫")


@router.callback_query(F.data == "check_data")
async def admin_check_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите юзернейм пользователя.")
    await state.set_state(st.Admin_Panel.waiting_username)
    await callback.answer()


@router.message(st.Admin_Panel.waiting_username)
async def admin_panel_get_username(message: Message, state: FSMContext):
    username = message.text.strip().lstrip('@')
    user_data = db.get_data(username)
    if not user_data:
        await message.answer(f"Пользователь с юзернеймом {username} не найден.")
    else:
        name, surname, user_id = user_data
        await message.answer(f"Данные пользователя: {username}\n"
                            f"Имя: {name}\n"
                            f"Фамилия: {surname}\n"
                            f"ID пользователя: {user_id}")

    await state.clear()
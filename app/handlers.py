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


@router.message(F.text == "📝Начать регистрацию")
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
async def admin_check_data(callback: CallbackQuery):
    users = db.get_usernames()
    if not users:
        await callback.message.edit_text("Нет пользователей для просмотра.", reply_markup=kb.return_button)
    else:
        await callback.message.edit_text("Выберите пользователя.", reply_markup= await kb.users(False))
        await callback.answer()


@router.callback_query(F.data == "delete_data")
async def admin_delete_data(callback: CallbackQuery):
    users = db.get_usernames()
    if not users:
        await callback.message.edit_text("Нет пользователей для удаления.", reply_markup=kb.return_button)
    else:
        await callback.message.edit_text("Выберите пользователя.", reply_markup= await kb.users(True))
        await callback.answer()


@router.callback_query(F.data.startswith("check_user_"))
async def admin_show_data(callback: CallbackQuery):
    username = callback.data.replace("check_user_", "")
    user_data = db.get_data(username)
    if not user_data:
        await callback.message.edit_text("По данному пользователю нету данных.", reply_markup=kb.return_button)
    else:
        user_id, name, surname = user_data
        await callback.message.edit_text("Данные пользователя:\n"
                                            f"ID пользователя: {user_id}\n"
                                            f"Имя: {name}\n"
                                            f"Фамилия: {surname}\n", reply_markup=kb.return_button)
    await callback.answer()


@router.callback_query(F.data.startswith("delete_user_"))
async def admin_delete_user_data(callback: CallbackQuery, state: FSMContext):
    username = callback.data.replace("delete_user_", "")
    user_data = db.get_data(username)
    if not user_data:
        await callback.message.edit_text("У данного пользователя нету данных для удаления.", reply_markup=kb.return_button)
    else:
        user_id, name, surname = user_data
        await callback.message.edit_text("Данные пользователя:\n"
                                    f"ID пользователя: {user_id}\n"
                                    f"Имя: {name}\n"
                                    f"Фамилия: {surname}\n"
                                    "Вы действительно хотите удалить данные?", reply_markup=kb.confirm_button)
        await state.set_state(st.Confirm_Delete.waiting_confirm)
        await state.update_data(username=username)
    await callback.answer()
        


@router.callback_query(st.Confirm_Delete.waiting_confirm, F.data == "confirm_yes")
async def delete_confirm_yes(callback: CallbackQuery, state: FSMContext):
    username = await state.get_data()
    db.delete_data(username["username"])
    await callback.message.edit_text("Данные пользователя удалены.", reply_markup=kb.admin_panel)
    await callback.answer()
    await state.clear()


@router.callback_query(st.Confirm_Delete.waiting_confirm, F.data == "confirm_no")
async def delete_confirm_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Хорошо. Возвращаемся обратно в панель", reply_markup=kb.admin_panel)
    await callback.answer()
    await state.clear()
    

@router.callback_query(F.data == "return")
async def admin_return_to_users(callback: CallbackQuery):
    await callback.message.edit_text("Вы вошли в админскую панель.", reply_markup= kb.admin_panel)
    await callback.answer()
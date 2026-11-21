from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    waiting_name = State()
    waiting_surname = State()

class Confirm_Delete(StatesGroup):
    waiting_confirm = State()
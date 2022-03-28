from aiogram.dispatcher.filters.state import StatesGroup, State


class MemberInfo(StatesGroup):
    profile = State()
    aria = State()
    specialization = State()
    experience = State()


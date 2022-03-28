from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.default import role_keyboard
from keyboards.inline.inline import link_keybord
from loader import dp


@dp.message_handler(Text(equals=["Частное лицо", "Организация"]))
async def individual_or_private(message: types.Message):
    if message.text == "Частное лицо":
        await message.answer("Наша цель, по сути, чтобы убрать клавиатуру снизу",
                             reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Наша миссия", reply_markup=link_keybord)
    else:
        await message.answer("Выберите, пожалуйста, один из вариантов", reply_markup=role_keyboard)


# @dp.message_handler(Text(equals=["Участник команды"]))
# async def click_member_of_team(message: types.Message):
#     await message.answer("Наша цель, по сути, чтобы убрать клавиатуру снизу", reply_markup=types.ReplyKeyboardRemove())
#     await message.answer("Наша миссия", reply_markup=link_keybord)


@dp.message_handler(Text(equals=
                         ["Сторонний эксперт", "Потенциальный партнер", "Представитель прессы", "Будущий инвестор"]))
async def click_member_of_team(message: types.Message):
    await message.answer(f"Тут мы сохраняем данные в таблицу, username {message.from_user.username}, "
                         f"но до этого тут будет какой-то опросник")

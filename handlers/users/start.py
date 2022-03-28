from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.default import individual_or_private_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Добрый день, {message.from_user.full_name}!\nКак вы себя определяете?",
                         reply_markup=individual_or_private_keyboard)


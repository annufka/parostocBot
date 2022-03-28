from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp, Text, Command

from loader import dp
from states.member_state import MemberInfo


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))


@dp.message_handler(Command("cancel"), state=MemberInfo.profile)
@dp.message_handler(Command("cancel"), state=MemberInfo.aria)
@dp.message_handler(Command("cancel"), state=MemberInfo.specialization)
@dp.message_handler(Command("cancel"), state=MemberInfo.experience)
async def bot_cancel(message: types.Message, state: FSMContext):
    await state.finish()
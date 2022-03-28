from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.default import profile_keyboard, technically_specialisation_keyboard, \
    not_technically_specialisation_keyboard, language_keybord, marketing_keybord, pm_keybord, design_keybord, \
    expirience_keybord
from keyboards.inline.inline import slack_keybord, question_keybord
from loader import dp
from states.member_state import MemberInfo


@dp.callback_query_handler(Text(equals="check_knowledge"))
async def check_knowledge(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Что вы будете делать в случае возникновения проблемы, которая блокирует вашу "
                                     "работу", reply_markup=question_keybord)



@dp.callback_query_handler(Text(equals=["alone", "mentor"]))
async def agree(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Пересмотрите еще раз правила и вернитесь к вопросу",
                                     reply_markup=question_keybord)


@dp.callback_query_handler(Text(equals=["alone", "mentor"]), state=None)
async def agree(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Молодец, вы правильно ответили на вопрос!\nПройдите небольшой опрос")
    await callback.message.answer("Укажите ваш профиль", reply_markup=profile_keyboard)
    await MemberInfo.profile.set()


@dp.message_handler(state=MemberInfo.profile)
async def not_or_technically_member(message: types.Message, state: FSMContext):
    await state.update_data(profile=message.text)
    await message.answer(
        f"Укажите вашу {'техническую' if message.text == 'Технический' else 'нетехническую'} специализацию",
        reply_markup=(technically_specialisation_keyboard if message.text == 'Технический' else
                      not_technically_specialisation_keyboard))
    await MemberInfo.next()


@dp.message_handler(state=MemberInfo.aria)
async def aria_of_member(message: types.message, state: FSMContext):
    await state.update_data(aria=message.text)
    data = await state.get_data()
    if data["profile"] == "Технический":
        if message.text == "Разработчик":
            await message.answer("Укажите вашу специализацию/язык программирования.\nЕсли вашего языка нет в списке, "
                                                                       "то укажите его", reply_markup=language_keybord)
        else:
            await message.answer("Укажите вашу специализацию/язык программирования",
                                 reply_markup=types.ReplyKeyboardRemove())
    else:
        if message.text == "Маркетинг":
            await message.answer("Укажите вашу специализацию", reply_markup=marketing_keybord)
        elif message.text == "ПМ":
            await message.answer("Укажите вашу специализацию", reply_markup=pm_keybord)
        elif message.text == "Дизайн":
            await message.answer("Укажите вашу специализацию", reply_markup=design_keybord)
        else:
            await message.answer("Укажите вашу специализацию", reply_markup=types.ReplyKeyboardRemove())
    await MemberInfo.next()


@dp.message_handler(state=MemberInfo.specialization)
async def specialization_of_member(message: types.Message, state: FSMContext):
    await state.update_data(specialization=message.text)
    await message.answer("Укажите ваш опыт", reply_markup=expirience_keybord)
    await MemberInfo.next()


@dp.message_handler(state=MemberInfo.experience)
async def experience_of_member(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    data = await state.get_data()
    # эти данные надо в таблицу с юзернеймом я так полагаю или все таки номер?
    await message.answer("Благодарственная речь за пройденный опрос", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Ссылка-приглашение в Слак с описанием как мы коммуницируем", reply_markup=slack_keybord)
    await state.finish()
    await write_data_to_google(data)

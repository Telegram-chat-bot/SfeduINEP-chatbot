from loader import dp,bot,db
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from states.state_machine import Admin_State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data import config
from keyboards.inline.buttons import back_btn, admin_menu, choose_level

query = []

@dp.message_handler(state='*', commands='exit')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_command(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.answer('Выхожу из команды...')

@dp.message_handler(commands="login")
async def admin_login(message: Message, state: FSMContext):
    admin_login = [k for k,v in config.ADMIN_DATA.items()]

    if str(message.from_user.id) in admin_login:
        await message.answer("Введите пароль")
        await Admin_State.get_password.set()
    else:
        await message.answer("Вы не являетесь админом, кыш отсюда")
        await state.finish()


@dp.message_handler(state=Admin_State.get_password)
async def get_password(message: Message, state: FSMContext):
    password = message.text

    if config.ADMIN_DATA[str(message.from_user.id)] == password:
        await message.answer("Вы вошли")
        await message.answer("Выберите раздел для редактирования", reply_markup=admin_menu)
        await state.finish()
    else:
        await message.answer("Неверный пароль")


@dp.callback_query_handler(lambda call: call.data in [
    "admission-admission_rules", "admission-submit_doc",
    "admission-passing_scores", "admission-number_of_places",
    "admission-achievements", "admission-special_rights",
    "admission-admission_stat", "admission-enrollment_proc",
    "about-acquaintance", "about-excursion",
    "about-events", "about-science",
    "about-partners_work", "about-stud_council",
    "about-photo", "about-map",
    "about-contacts", "questions-faq"
])
async def choose_block(call: CallbackQuery):
    if call.data in ["admission-passing_scores", "admission-number_of_places", "direct_prep"]:
        await call.message.edit_text("Выберите направление подготовки", reply_markup=choose_level)

    else:
        await call.message.answer("Напишите новый текст для статьи")
        await call.message.delete_reply_markup()

        query.clear()
        query.append(call.data.split("-"))

        await Admin_State.edit_inf.set()

@dp.callback_query_handler(lambda call: call.data in ["bak", "spec", "mag"])
async def edit_direct(call: CallbackQuery):
    if call.data == "bak":
        await call.message.answer("Напишите код и через пробел описание")
        await Admin_State.edit_btn.set()

@dp.message_handler(state=Admin_State.edit_btn)
async def edit_btn(message: Message):
    new_btn = message.text.split("\n")
    d = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=new_btn[-1], callback_data=new_btn[0])
            ]
        ]
    )
    await message.answer("sdcdf", reply_markup=d)

@dp.message_handler(state=Admin_State.edit_inf)
async def get_text(message: Message, state: FSMContext):
    text = message.text
    try:
        await db.add_data(inf=text, block=query[0][0], element=query[0][1])
        await db.update_data(inf=text, block=query[0][0], element=query[0][1])

        await message.answer("Данные успешно обновлены. Хотите ещё отредактировать что-нибудь?", reply_markup=admin_menu)
    except Exception as e:
        await message.answer(f"Ошибка\n{e}")
    await state.finish()
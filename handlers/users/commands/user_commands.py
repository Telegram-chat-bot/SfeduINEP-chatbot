from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Command

from django_admin.service.models import Users
from filters.ChatTypeFilter import IsChat
from loader import dp, DEBUG
from aiogram.types import Message

from utils.db_api.db_commands import Database
from django_admin.bot.models import Welcome_message, Help_content

from keyboards.default import enrollee_menu as kb


# * обработчик для команды выхода из состояния пользовательского ввода
@dp.message_handler(Command("exit"), state="*")
async def exit_input_mode(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Ввод текста отменён")


# * СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(IsChat(), CommandStart())
async def welcome(message: Message):
    content: str = await Database(Welcome_message).get_field_by_name("message")
    await message.answer(
        content,
        reply_markup=await kb.generate_keyboard(one_time_keyboard=True)
    )
    await Database(Users).add_user(
        username=' '.join(
            [
                message.from_user.first_name or "",
                message.from_user.last_name or ""
            ]
        ),
        user_id=int(message.from_user.id)
    )


@dp.message_handler(IsChat(), Command("help"))
async def help_command(message: Message):
    content = Help_content.objects.filter(target_user=message.chat.type).first().content
    await message.answer(content or "В этот раздел еще не добавили информацию")


@dp.message_handler(Command("get_id"))
async def get_userid(message: Message):
    if DEBUG:
        await message.answer(message.from_user.id)

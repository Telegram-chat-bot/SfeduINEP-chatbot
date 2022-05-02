from aiogram.dispatcher.filters import CommandStart, Command

from filters.ChatTypeFilter import IsChat
from loader import dp
from aiogram.types import Message

from utils.db_api.db_commands import Database, add_user, get_help_text
from django_admin.bot.models import Welcome_message

from keyboards.default import enrollee_menu as kb

db = Database(Welcome_message)


# СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(IsChat(), CommandStart())
async def welcome(message: Message):
    await message.answer(
        await db.get_field_by_name("message"),
        reply_markup=kb.main_menu
    )

    await add_user(
        name=' '.join(
            [
                message.from_user.first_name or "",
                message.from_user.last_name or ""
            ]
        ),
        uid=int(message.from_user.id)
    )


@dp.message_handler(IsChat(), Command("help"))
async def help_command(message: Message):
    await message.answer(
        await get_help_text(message.chat.type)
    )

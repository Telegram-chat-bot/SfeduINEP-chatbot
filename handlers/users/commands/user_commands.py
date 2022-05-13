from aiogram.dispatcher.filters import CommandStart, Command

from django_admin.service.models import Users
from filters.ChatTypeFilter import IsChat
from loader import dp
from aiogram.types import Message

from utils.db_api.db_commands import Database
from django_admin.bot.models import Welcome_message, Help_content

from keyboards.default import enrollee_menu as kb


# СТАРТОВОЕ СООБЩЕНИЕ
@dp.message_handler(IsChat(), CommandStart())
async def welcome(message: Message):
    content = Database(Welcome_message)
    await message.answer(
        await content.get_field_by_name("message"),
        reply_markup=kb.main_menu
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
    content = Help_content.objects.filter(
        target_user=message.chat.type
    ).first().content
    await message.answer(
        content or "В этот раздел еще не добавили информацию"
    )

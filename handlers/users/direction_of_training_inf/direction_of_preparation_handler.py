from loader import bot, dp
from aiogram.types import CallbackQuery, message, InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline import buttons as btn

def init_url(link):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Перейти к источнику",
                    url=link
                )
            ],
            [
                btn.back_btn
            ]
        ]
    )

@dp.callback_query_handler(lambda call: call.data)
async def test(call: CallbackQuery):
    for direction, link in directions.items():
        if call.data == direction:
            await call.message.edit_text("Всю информацию по данному направлению вы можете найти, перейдя по ссылке", reply_markup=init_url(link=link))



directions = {
    "11.03.03": "https://inep.sfedu.ru/chairs/kes/",
    "11.03.04": "https://inep.sfedu.ru/chairs/rte/",
    "12.03.01": "https://inep.sfedu.ru/chairs/egaimt/egaimt-abiturient/#120304",
    "12.03.04": "https://inep.sfedu.ru/chairs/egaimt/egaimt-abiturient/#120304",
    "20.03.01": "https://inep.sfedu.ru/chairs/tbh/tbh-abiturient/",
    "21.03.02": "https://inep.sfedu.ru/chairs/iitis/iitis-abitur/",
    "28.03.01": "https://inep.sfedu.ru/chairs/ntmst/ntmst-abiturient/"
}


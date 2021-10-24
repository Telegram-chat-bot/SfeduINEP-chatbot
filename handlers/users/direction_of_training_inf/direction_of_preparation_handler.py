from loader import bot, dp
from aiogram.types import CallbackQuery, message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext

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
async def direct_of_prepare_handler(call: CallbackQuery, state: FSMContext):
    for direction, link in directions.items():
        if call.data == direction:
            await call.message.edit_text("Всю информацию по данному направлению вы можете найти, перейдя по ссылке", reply_markup=init_url(link=link))


directions = {
    #Бакалавриат
    "11.03.03": "https://inep.sfedu.ru/chairs/kes/",
    "11.03.04": "https://inep.sfedu.ru/chairs/rte/",
    "12.03.01": "https://inep.sfedu.ru/chairs/egaimt/egaimt-abiturient/#120304",
    "12.03.04": "https://inep.sfedu.ru/chairs/egaimt/egaimt-abiturient/#120304",
    "20.03.01": "https://inep.sfedu.ru/chairs/tbh/tbh-abiturient/",
    "21.03.02": "https://inep.sfedu.ru/chairs/iitis/iitis-abitur/",
    "28.03.01": "https://inep.sfedu.ru/chairs/ntmst/ntmst-abiturient/",
    
    #Специалитет
    "26.05.04": "https://inep.sfedu.ru/wp-content/uploads/2014/12/05/buklet_26-05-04-111.pdf",

    #Магистратура
    "11.04.03": "https://inep.sfedu.ru/chairs/kes/#11.04.03",
    "11.04.04": "https://inep.sfedu.ru/chairs/rte/rte-abiturient/#110404",
    "12.04.01": "https://sfedu.ru/www/stat_pages22.show?p=EDU/annot/D&params=%28p_specia_id=%3E3892%29",
    "12.04.04": "https://sfedu.ru/www/stat_pages22.show?p=EDU/annot/D&params=%28p_specia_id=%3E3894%29",
    "20.04.01": "https://inep.sfedu.ru/wp-content/uploads/2014/12/08/%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%BD%D0%B0%D1%8F-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C.pdf",
    "28.04.01": "https://sfedu.ru/www/stat_pages22.show?p=EDU/annot/D&params=%28p_specia_id=%3E3908%29"
}


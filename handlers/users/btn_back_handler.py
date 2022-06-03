from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp

from keyboards.inline import buttons as btn
from states.state_machine import PositionState


@dp.callback_query_handler(lambda call: call.data == "back_to")
async def back_btn_handler(call: CallbackQuery, state: FSMContext):
    await state.set_state(PositionState.set_pressed_btn)

    await PositionState.get_pressed_btn.set()
    await call.message.edit_text("Выберите уровень подготовки", reply_markup=btn.choose_level)

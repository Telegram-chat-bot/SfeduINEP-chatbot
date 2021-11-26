from aiogram.dispatcher.filters.state import State, StatesGroup

class User_State(StatesGroup):
    get_pressed_button = State()
    question = State()
    direction = State()
    question_direction = State()
    
class AdminState(StatesGroup):
    get_id = State()
    get_answer = State()
from aiogram.dispatcher.filters.state import State, StatesGroup

class User_State(StatesGroup):
    get_pressed_button = State()
    
    direction = State()
    
    question = State()
    question_direction = State()
    
    message_id = State()
    get_message_id = State()
    
class AdminState(StatesGroup):
    get_id = State()
    get_answer = State()
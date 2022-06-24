from aiogram.dispatcher.filters.state import State, StatesGroup


class PositionState(StatesGroup):
    set_pressed_btn = State()
    get_pressed_btn = State()


class UserState(StatesGroup):
    direction = State()
    get_info_for_question = State()


class Questions(StatesGroup):
    user_question = State()
    user_question_dir = State()
    answer = State()
    get_answer = State()


class GroupState(StatesGroup):
    attention_message = State()


class Feedback(StatesGroup):
    feedback_message = State()
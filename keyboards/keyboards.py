from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# ------ Creating keyboard via ReplyKeyboardBuilder -----

# Creating buttons with positive or negative answers
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Initializing builder for keyboard with buttons "Go" and "Dont want"
yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True,
)

# ----- Creating gaming keyboard without ReplyKeyboardBuilder -----

# Creating buttons for gaming keyboard
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# Crating keyboard
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)

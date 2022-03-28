from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

individual_or_private_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Частное лицо")
        ],
        [
            KeyboardButton(text="Организация")
        ],
    ]
)

role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        # [
        #     KeyboardButton(text="Участник команды")
        # ],
        [
            KeyboardButton(text="Сторонний эксперт")
        ],
        [
            KeyboardButton(text="Потенциальный партнер")
        ],
        [
            KeyboardButton(text="Представитель прессы")
        ],
        [
            KeyboardButton(text="Будущий инвестор")
        ],

    ],
    resize_keyboard=True
)

profile_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Технический")
        ],
        [
            KeyboardButton(text="Нетехнический")
        ],
    ],
    resize_keyboard=True
)

technically_specialisation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Разработчик")
        ],
        [
            KeyboardButton(text="Девопс")
        ],
        [
            KeyboardButton(text="Тестировщик")
        ],
        [
            KeyboardButton(text="Прочее")
        ],
    ],
    resize_keyboard=True
)

not_technically_specialisation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Маркетинг")
        ],
        [
            KeyboardButton(text="ПМ")
        ],
        [
            KeyboardButton(text="Дизайн")
        ],
        [
            KeyboardButton(text="Прочее")
        ],
    ],
    resize_keyboard=True
)

language_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="C / C++ / Embedded")
        ],
        [
            KeyboardButton(text="JavaScript / Front-End")
        ],
        [
            KeyboardButton(text="Node.js")
        ],
        [
            KeyboardButton(text="Python")
        ],
    ]
)

marketing_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lead Generation")
        ],
        [
            KeyboardButton(text="Sales")
        ],
        [
            KeyboardButton(text="Marketing")
        ],
    ]
)

pm_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Scrum Master/Agile Coach")
        ],
        [
            KeyboardButton(text="Project Manager")
        ],
        [
            KeyboardButton(text="Product Manager")
        ],
    ]
)

design_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Design / UI/UX")
        ],
        [
            KeyboardButton(text="2D/3D Artist / Illustrator")
        ],
    ]
)

expirience_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Без опыта")
        ],
        [
            KeyboardButton(text="Прохожу обучение")
        ],
        [
            KeyboardButton(text="До 1 года")
        ],
        [
            KeyboardButton(text="Больше 1 года")
        ],
    ]
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import URL_RULES, SLACK_LINK

link_keybord = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Правила сообщества", url=URL_RULES)
        ],
        [
            InlineKeyboardButton(text="Проверка знаний", callback_data="check_knowledge")
        ],
    ])

# с этой клавиатурой пока  не известно
question_keybord = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Буду гуглить и искать решение", callback_data="alone")
        ],
        [
            InlineKeyboardButton(text="Напишу в общий чат в slack", callback_data="team")
        ],
        [
            InlineKeyboardButton(text="Напишу кому-то в личку в slack", callback_data="mentor")
        ],
    ])

slack_keybord = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Подключиться в Slack", url=SLACK_LINK)
    ]
])
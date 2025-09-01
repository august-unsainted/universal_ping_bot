from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_btn(text: str, callback: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=callback)


def get_keyboard(sender: int) -> InlineKeyboardMarkup:
    row = []
    for text, data in (('Да ✅', 'confirm'), ('Отменить ❌', 'cancel')):
        row.append(get_btn(text, f'{data}_{sender}'))
    return InlineKeyboardMarkup(inline_keyboard=[row])


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➕ Добавить бота в группу',
                          url='https://t.me/UniversalPingBot?startgroup=true')],
    [get_btn('🧑‍💻 Об авторах', 'developers')]])
back_kb = InlineKeyboardMarkup(inline_keyboard=[[get_btn('⬅️ Назад', 'start')]])

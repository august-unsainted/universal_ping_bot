from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

invent_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='➕ Добавить бота в группу',
                          url='https://t.me/UniversalPingBot?startgroup=true')]])


def get_btn(text: str, callback: str, sender: int) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=f'{callback}_{sender}')


def get_keyboard(sender: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[get_btn('Да ✅', 'confirm', sender),
                                                  get_btn('Отменить ❌', 'cancel', sender)]])

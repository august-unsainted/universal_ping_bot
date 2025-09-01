from pathlib import Path
from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from orjson import orjson
from pyrogram.types import InlineKeyboardMarkup

from utils.keyboards import get_keyboard, start_kb
from utils.get_members import get_chat_members, get_emoji

router = Router()
messages = orjson.loads((Path.cwd() / 'messages.json').read_bytes())


def get_func(message: Message) -> callable:
    content = message.reply_to_message
    return content.reply if content else message.answer


async def deny_action(callback: CallbackQuery) -> bool:
    res = callback.from_user.id != int(callback.data.split('_')[-1])
    if res:
        await callback.answer('Вы не можете выполнить это действие — команда /all была выполнена не вами.', show_alert=True)
    return res


async def handle_edit_message(callback: CallbackQuery, text: str, kb: InlineKeyboardMarkup) -> None:
    args = {'text': text, 'reply_markup': kb, 'parse_mode': 'HTML'}
    try:
        await callback.message.edit_text(**args)
    except TelegramBadRequest:
        await callback.message.answer(**args)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(messages.get('start'), reply_markup=start_kb)


@router.callback_query(F.data == 'start')
async def start_callback(callback: CallbackQuery):
    await handle_edit_message(callback, messages.get('start'), start_kb)


@router.message(Command('all'))
async def cmd_all(message: Message):
    if message.chat.id > 0:
        await message.answer(messages.get('all'))
        return
    func = get_func(message)
    await func(messages.get('confirm').format(message.from_user.username),
               reply_markup=get_keyboard(message.from_user.id))
    await message.delete()


@router.callback_query(F.data.startswith('confirm'))
async def confirm_ping(callback: CallbackQuery):
    if await deny_action(callback):
        return
    message = callback.message
    func = get_func(message)
    await func(messages.get('text').format(callback.from_user.username), parse_mode='HTML')
    await message.delete()
    members = [get_emoji(member) for member in await get_chat_members(chat_id=message.chat.id) if
               member != callback.from_user.id]
    for i in range(0, len(members), 5):
        await message.answer(''.join(members[i:i + 5]), parse_mode='HTML')


@router.callback_query(F.data.startswith('cancel'))
async def cancel_ping(callback: CallbackQuery):
    if not await deny_action(callback):
        await callback.message.delete()

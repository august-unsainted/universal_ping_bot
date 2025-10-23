import random

from aiogram.types import CallbackQuery
from telethon import TelegramClient

from config import *

client = TelegramClient('Universal Ping', API_ID, API_HASH)


async def on_startup():
    await client.start(bot_token=TOKEN)


async def on_shutdown():
    await client.disconnect()


async def get_chat_members(callback: CallbackQuery) -> list[str]:
    chat_members = []
    async for member in client.iter_participants(callback.message.chat.id):
        chat_members.append((member.id, member.username))
    temp_emoji = EMOJI.split()
    result = []
    for member, member_username in chat_members:
        member_username = member_username or ''
        if member != callback.from_user.id and not member_username.lower().endswith('bot'):
            # and not member.lower().endswith('bot')
            index = random.randint(0, len(temp_emoji) - 1)
            result.append(f'<a href="tg://user?id={member}">{temp_emoji.pop(index)}</a>')
    return result

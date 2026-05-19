import random

from aiogram.types import CallbackQuery
from telethon import TelegramClient
from telethon.errors import RPCError

from config import *

client = TelegramClient('Universal Ping', API_ID, API_HASH)


async def on_startup():
    await client.start(bot_token=TOKEN)


async def on_shutdown():
    await client.disconnect()


async def get_participants(chat_id):
    chat_members = []
    try:
        async for member in client.iter_participants(chat_id, limit=100, aggressive=False):
            chat_members.append((member.id, member.username))
    except (ConnectionError, OSError, RPCError):
        await on_startup()
    return chat_members


async def get_chat_members(callback: CallbackQuery) -> list[str]:
    chat_members = []
    attempt = 1
    while not chat_members and attempt <= 3:
        chat_members = await get_participants(callback.message.chat.id)
        attempt += 1
    temp_emoji = EMOJI.split()
    result = []
    for member, member_username in chat_members:
        member_username = member_username or ''
        if member != callback.from_user.id and not member_username.lower().endswith('bot'):
            index = random.randint(0, len(temp_emoji) - 1)
            result.append(f'<a href="tg://user?id={member}">{temp_emoji.pop(index)}</a>')
    return result

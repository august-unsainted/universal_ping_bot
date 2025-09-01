import random
from telethon import TelegramClient
from config import *

client = TelegramClient('Universal Ping', API_ID, API_HASH)


async def get_chat_members(chat_id: str | int):
    await client.start(bot_token=TOKEN)
    chat_members = []
    async for member in client.iter_participants(chat_id):
        chat_members.append(member.id)
    await client.disconnect()
    return chat_members


def get_emoji(user_id: int) -> str:
    member_emoji = EMOJI[random.randint(0, len(EMOJI) - 1)]
    return f'<a href="tg://user?id={user_id}">{member_emoji}</a>'

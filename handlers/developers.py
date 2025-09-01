from aiogram import Router, F
from aiogram.types import CallbackQuery

from handlers.all import messages, handle_edit_message
from utils.keyboards import back_kb

router = Router()


@router.callback_query(F.data == 'developers')
async def about_developers(callback: CallbackQuery):
    await handle_edit_message(callback, messages.get('developers'), back_kb)

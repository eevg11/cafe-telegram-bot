from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards import inline_kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Hi, {message.from_user.first_name}! Welcome to our cafe. ☕", 
        reply_markup=inline_kb.main_menu_kb()
    )

@router.callback_query(F.data == "main_menu")
async def go_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "Main Menu:", 
        reply_markup=inline_kb.main_menu_kb()
    )
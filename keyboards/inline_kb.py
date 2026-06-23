from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="☕ View Menu", callback_data="view_menu"))
    builder.row(InlineKeyboardButton(text="🛒 My Cart", callback_data="view_cart"))
    return builder.as_markup()

def menu_items_kb(products) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for prod_id, name, price in products:
        builder.row(InlineKeyboardButton(text=f"{name} — {price} UAH", callback_data=f"buy_{prod_id}"))
    builder.row(InlineKeyboardButton(text="⬅️ Back", callback_data="main_menu"))
    return builder.as_markup()

def cart_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="✅ Checkout", callback_data="checkout"))
    builder.row(InlineKeyboardButton(text="🗑 Clear Cart", callback_data="clear_cart"))
    builder.row(InlineKeyboardButton(text="⬅️ To Menu", callback_data="view_menu"))
    return builder.as_markup()
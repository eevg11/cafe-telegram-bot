from aiogram import Router, F
from aiogram.types import CallbackQuery
from database import db
from keyboards import inline_kb

router = Router()

@router.callback_query(F.data == "view_menu")
async def show_menu(callback: CallbackQuery):
    products = db.get_menu()
    await callback.message.edit_text(
        "Select items to add to your cart:", 
        reply_markup=inline_kb.menu_items_kb(products)
    )

@router.callback_query(F.data.startswith("buy_"))
async def add_item_to_cart(callback: CallbackQuery):
    product_id = int(callback.data.split("_")[1])
    db.add_to_cart(user_id=callback.from_user.id, product_id=product_id)
    await callback.answer("Added to cart! ✅") 

@router.callback_query(F.data == "view_cart")
async def show_cart(callback: CallbackQuery):
    cart_items = db.get_cart(callback.from_user.id)
    
    if not cart_items:
        await callback.message.edit_text(
            "Your cart is empty 🕸", 
            reply_markup=inline_kb.main_menu_kb()
        )
        return
        
    text = "🛒 **Your Cart:**\n\n"
    total_sum = 0
    for name, price, qty in cart_items:
        item_sum = price * qty
        total_sum += item_sum
        text += f"• {name} x{qty} = {item_sum} UAH\n"
    text += f"\n**Total: {total_sum} UAH**"
    
    await callback.message.edit_text(
        text, 
        parse_mode="Markdown", 
        reply_markup=inline_kb.cart_kb()
    )

@router.callback_query(F.data == "clear_cart")
async def clear_cart_handler(callback: CallbackQuery):
    db.clear_cart(callback.from_user.id)
    await callback.answer("Cart cleared")
    await callback.message.edit_text(
        "Your cart is empty 🕸", 
        reply_markup=inline_kb.main_menu_kb()
    )

@router.callback_query(F.data == "checkout")
async def checkout_handler(callback: CallbackQuery):
    db.clear_cart(callback.from_user.id)
    await callback.message.edit_text(
        "🎉 Thank you for your order! Our barista is already preparing it.", 
        reply_markup=inline_kb.main_menu_kb()
    )
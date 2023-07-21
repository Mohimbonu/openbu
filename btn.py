
from aiogram import types


async def choose_btn():
    btn = types.InlineKeyboardMarkup()
    btn.add(
        types.InlineKeyboardButton("🗳 Ovoz berish", callback_data="Ovoz berish"),

    )
    btn.add(
        types.InlineKeyboardButton("💰 Balans", callback_data="Balans"),
    )
    btn.add(
        types.InlineKeyboardButton("📝 Qo'llanma", callback_data="Qo'llanma"),
    )


    return btn
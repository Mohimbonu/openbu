from aiogram import types


async def start_btn():
    btn = types.ReplyKeyboardMarkup()
    btn.add(
        types.KeyboardButton("🗳 Ovoz berish"),
        types.KeyboardButton("💰 Balans"),
        types.KeyboardButton("🔗 Referal ssilka"),
        types.KeyboardButton("📝 Qo'llanma"),

    )
    return btn
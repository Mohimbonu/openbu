import logging
from aiogram import Bot, Dispatcher, executor, types
from reply_btn import start_btn
from btn import choose_btn

logging.basicConfig(level=logging.INFO)
BOT_TOKEN =''
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)                                                                                                                                             
dp = Dispatcher(bot=bot)

async def set_bot_commands(dp: Dispatcher):
    await dp.bot.set_my_commands (
        [
            types.BotCommand("start","🔥Pul ishlash🔥"),
        ]
    )                                                   



@dp.message_handler(commands=['start'])
async def start_bot_commandr(message: types.Message):
    btn = await start_btn()    
    await message.answer("<b>Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin. Unutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.Telefon raqamingizni +998901234567 shaklida yuboring.</b>")



@dp.message_handler(text="🗳 Ovoz berish")
async def start_bot_command(message: types.Message):
    btn = await choose_btn()
    await message.answer("📞 Ovoz berish uchun telefon raqamingizni kiriting: Na'muna: +998991234567 ✅ Ovoz berish muvaffaqiyatli o'tganda, hisobingizga o'tkazib beriladigan summa: 12000 UZS", reply_markup=btn)
     
     
if __name__ == "__main__" :
    executor.start_polling(dp, on_startup=set_bot_commands)
import re
from aiogram import Bot, types, Dispatcher,executor  # Bot - отвечает за работу с API, #Dispatcher - обработчик событий
TOKEN = '#88'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

Balance_of_wallet = 10000
Category_products = 0

@dp.message_handler()
async def echo0(message : types.Message):
    req = str(message.text).lower()
    if 'продукты' in req:
        text = message.text
        numb = re.findall('[0-9]+', text)
        text = int((numb[0]))
        global Category_products
        Category_products += text
        await message.answer('Расход в категорию "Продукты" записан')
        await message.answer(f'Траты по продуктам за месяц составляют ={Category_products} руб.')



async def starting(_):
    print("Бот вышел в онлайн")


#@dp.message_handler(commands=['2'])
#async def echo(message: types.Message):
    #await message.answer('Выполняю команду 2')


#@dp.message_handler()
#async def filter_message(message: types.Message):
    #await message.answer('Ругаться запрещено.')


#if __name__ == '__main__':
    #executor.start_polling(dp, skip_updates=False)
executor.start_polling(dp, skip_updates=True, on_startup=starting) # on_startup - сюда прописываем функцию, что будет выполняться при старте бота
#executor - модуль aiogram, что позволяет запустить бота
#на вебхуках или полинге

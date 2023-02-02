from aiogram import types
from module.base import cars_done


async def cars_list(message: types.Message):
    """
        Функция покажет пользователю команды
    """
    i = 0
    for i in range(len(cars_done())):
        car = cars_done()[i]

        await message.answer(text=f'''
Марка - {car[1]} 
Цена - {car[2]}
Информация - {car[3]}
Ссылка - {car[4]}
''')
        # sleep(3)
    await message.delete()
import asyncio
import logging
import aiogram
from aiogram import Dispatcher, Bot
from config_data.config import Config, load_config
from hendlers import other_hendlers, user_hendlers
from keyboards.main_menu_keyboard import set_main_menu_commands

# инициализируем логгер

logger = logging.getLogger(__name__)

# Функция конфигурирования и запуска бота
async def main():
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
                                '%(lineno)d - %(name)s - %(message)s'
                        )
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    # Настраиваем главное меню бота
    await set_main_menu_commands(bot)

    dp.include_router(user_hendlers.router)
    dp.include_router(other_hendlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
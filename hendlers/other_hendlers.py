from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def ather_answer_process(message: Message):
    await message.answer(f'команда {message.text} не распознана')
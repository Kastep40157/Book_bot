from copy import deepcopy
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON
from data_base.data_base import user_base__template, user_bd

router = Router()

@router.message(CommandStart())
async def command_start_process(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in user_bd:
        user_bd[message.from_user.id] = deepcopy(user_base__template)


@router.message(Command(commands='help'))
async def  command_help_process(message: Message):
    await message.answer(LEXICON[message.text])
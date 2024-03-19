from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    tg_bot: TgBot
    admin_ids: list[int]

# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token
def load_config(path: str | None=None ) -> Config:
    env: Env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')), admin_ids=list(map(int,env.list('ADMIN_IDS'))))

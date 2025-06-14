import os
import telebot
from telebot.types import BotCommand
from dotenv import load_dotenv
from collections import defaultdict

from config import config
from bot.handlers import register_handlers
from bot.ai_assistant import client, qa_chain, user_history
from bot.slider import SLIDERS, send_slider, edit_slider, clear_photos, user_last_photo_ids

# === Инициализация ===
load_dotenv()
bot = telebot.TeleBot(config.TOKEN)

# === Глобальные переменные ===
user_ai_mode = defaultdict(bool)
user_language = defaultdict(lambda: "ru")

# === Устанавливаем команды ===
bot.set_my_commands([
    BotCommand("start", "Начать / Start"),
    BotCommand("menu", "Показать меню"),
    BotCommand("lang", "Изменить язык"),
    BotCommand("ask_ai", "Спросить у ИИ 🤖"),
])

# === Регистрируем все обработчики ===
register_handlers(bot, user_language, user_ai_mode, user_history, client, qa_chain)

# === Запуск бота ===
bot.polling(none_stop=True)

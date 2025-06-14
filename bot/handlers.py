from telebot import types
from bot.slider import SLIDERS, send_slider, edit_slider, clear_photos, user_last_photo_ids
from collections import defaultdict

user_ai_mode = defaultdict(bool)
user_language = defaultdict(lambda: "ru")

def register_handlers(bot, user_language, user_ai_mode, user_history, client, qa_chain):
    @bot.message_handler(commands=["start"])
    def start(message):
        keyboard = types.InlineKeyboardMarkup()
        button11 = types.InlineKeyboardButton(text="Русский", callback_data="button11")
        button22 = types.InlineKeyboardButton(text="English", callback_data="button22")
        keyboard.add(button11)
        keyboard.add(button22)

        bot.send_message(
            message.chat.id,
            text=f"Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>, бот - Путеводитель. Выбери, то что тебя интересует",
            parse_mode='html',
            reply_markup=keyboard
        )

    @bot.message_handler(commands=["lang"])
    def lang_command(message):
        keyboard = types.InlineKeyboardMarkup()
        button11 = types.InlineKeyboardButton(text="Русский", callback_data="button11")
        button22 = types.InlineKeyboardButton(text="English", callback_data="button22")
        keyboard.add(button11, button22)
        bot.send_message(
            message.chat.id,
            "Пожалуйста, выберите язык / Please select your language:",
            reply_markup=keyboard
        )

    @bot.message_handler(commands=["ask_ai"])
    def ask_ai_command(message):
        user_ai_mode[message.chat.id] = True
        bot.send_message(message.chat.id, "🤖 Задай мне вопрос. ")

    @bot.message_handler(commands=["menu"])
    def menu_command(message):
        lang = user_language[message.chat.id]
        keyboard = types.InlineKeyboardMarkup()

        if lang == "ru":
            keyboard.add(types.InlineKeyboardButton(text="Туры", callback_data="button1"))
            keyboard.add(types.InlineKeyboardButton(text="Достопримечательности", callback_data="button2"))
            keyboard.add(types.InlineKeyboardButton(text="Отели", callback_data="button3"))
            keyboard.add(types.InlineKeyboardButton(text="Кафе", callback_data="button4"))
            keyboard.add(types.InlineKeyboardButton(text="\ud83d\udcde Полезные контакты", callback_data="button5"))
            keyboard.add(types.InlineKeyboardButton(text="\ud83e\udd16 Задать вопрос ИИ", callback_data="ask_ai"))
        else:
            keyboard.add(types.InlineKeyboardButton(text="Tours", callback_data="button1en"))
            keyboard.add(types.InlineKeyboardButton(text="Attractives", callback_data="button2en"))
            keyboard.add(types.InlineKeyboardButton(text="Hotels", callback_data="button3en"))
            keyboard.add(types.InlineKeyboardButton(text="Cafe", callback_data="button4en"))
            keyboard.add(types.InlineKeyboardButton(text="Useful Contacts", callback_data="button5en"))
            keyboard.add(types.InlineKeyboardButton(text="\ud83e\udd16 Ask AI", callback_data="ask_ai"))

        bot.send_message(message.chat.id, "Меню" if lang == "ru" else "Menu", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        lang = user_language[call.message.chat.id]

        if call.data == "button11":
            user_language[call.message.chat.id] = "ru"
            menu_command(call.message)
        elif call.data == "button22":
            user_language[call.message.chat.id] = "en"
            menu_command(call.message)
        elif call.data == "mainmenu":
            clear_photos(bot, call)
            menu_command(call.message)
        elif call.data == "mainmenuenglish":
            clear_photos(bot, call)
            menu_command(call.message)
        elif call.data == "ask_ai":
            user_ai_mode[call.message.chat.id] = True
            bot.send_message(call.message.chat.id, "Вы вошли в режим ИИ. Напишите ваш вопрос.")

        elif call.data in SLIDERS:
            send_slider(bot, call, call.data, lang)

        elif "_" in call.data:
            category, index = call.data.split("_")
            if category in SLIDERS:
                edit_slider(bot, call, category, int(index), lang)

        elif call.data in ["button1", "button1en"]:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(
                types.InlineKeyboardButton("Автотур" if lang == "ru" else "Auto Tour", callback_data="tour"),
                types.InlineKeyboardButton("Пеший тур" if lang == "ru" else "Hiking Tour", callback_data="tour")
            )
            back_text = "Назад в меню ⏪" if lang == "ru" else "⬅️ Back to menu"
            back_callback = "mainmenu" if lang == "ru" else "mainmenuenglish"
            keyboard.add(types.InlineKeyboardButton(back_text, callback_data=back_callback))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите тип тура 👇" if lang == "ru" else "Choose a tour 👇", reply_markup=keyboard)

        elif call.data in ["button2", "button2en"]:
            keyboard = types.InlineKeyboardMarkup()
            text = "Мечети / Церкви" if lang == "ru" else "Mosques / Churches"
            keyboard.add(types.InlineKeyboardButton(text, callback_data="sight"))
            back_text = "Назад в меню ⏪" if lang == "ru" else "⬅️ Back to menu"
            back_callback = "mainmenu" if lang == "ru" else "mainmenuenglish"
            keyboard.add(types.InlineKeyboardButton(back_text, callback_data=back_callback))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите достопримечательность 👇" if lang == "ru" else "Choose an attraction 👇",
                                  reply_markup=keyboard)

        elif call.data in ["button3", "button3en"]:
            keyboard = types.InlineKeyboardMarkup()
            labels = ["Отели", "Гостевые дома", "Хостелы"] if lang == "ru" else ["Hotels", "Guesthouses", "Hostels"]
            ids = ["hotel", "guest", "hostel"]
            for label, cid in zip(labels, ids):
                keyboard.add(types.InlineKeyboardButton(label, callback_data=cid))
            back_text = "Назад в меню ⏪" if lang == "ru" else "⬅️ Back to menu"
            back_callback = "mainmenu" if lang == "ru" else "mainmenuenglish"
            keyboard.add(types.InlineKeyboardButton(back_text, callback_data=back_callback))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите тип проживания 👇" if lang == "ru" else "Choose where to stay 👇",
                                  reply_markup=keyboard)

        elif call.data in ["button4", "button4en"]:
            keyboard = types.InlineKeyboardMarkup()
            labels = ["Кафе", "Кофейни", "Ашлян-фу"] if lang == "ru" else ["Cafe", "Coffee shops", "Ashlyan-fu"]
            ids = ["cafe", "coffee", "ashlyan"]
            for label, cid in zip(labels, ids):
                keyboard.add(types.InlineKeyboardButton(label, callback_data=cid))
            back_text = "Назад в меню ⏪" if lang == "ru" else "⬅️ Back to menu"
            back_callback = "mainmenu" if lang == "ru" else "mainmenuenglish"
            keyboard.add(types.InlineKeyboardButton(back_text, callback_data=back_callback))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите заведение 👇" if lang == "ru" else "Choose a place 👇",
                                  reply_markup=keyboard)

        elif call.data in ["button5", "button5en"]:
            contact_text = (
                "<b>\ud83d\udcde Полезные контакты</b>\n\n"
                "\ud83d\ude93 <b>Полиция:</b> 102\n"
                "\ud83d\ude91 <b>Скорая помощь:</b> 103\n"
                "\ud83d\ude92 <b>Пожарная служба:</b> 101\n"
                "\ud83c\udfe5 <b>Городская больница Каракола:</b> +996 312 00 00 00\n"
                "\u2139\ufe0f <b>Туристический инфоцентр:</b> +996 700 123 456\n"
                "\ud83d\ude96 <b>Такси:</b> +996 777 123 456"
            ) if lang == "ru" else (
                "<b>\ud83d\udcde Useful Contacts</b>\n\n"
                "\ud83d\ude93 <b>Police:</b> 102\n"
                "\ud83d\ude91 <b>Ambulance:</b> 103\n"
                "\ud83d\ude92 <b>Fire Service:</b> 101\n"
                "\ud83c\udfe5 <b>Karakol City Hospital:</b> +996 312 00 00 00\n"
                "\u2139\ufe0f <b>Tourist Info Center:</b> +996 700 123 456\n"
                "\ud83d\ude96 <b>Taxi Service:</b> +996 777 123 456"
            )
            back_callback = "mainmenu" if lang == "ru" else "mainmenuenglish"
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton("⏪ Назад в меню" if lang == "ru" else "⬅️ Back to menu", callback_data=back_callback))
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=contact_text,
                parse_mode="HTML",
                reply_markup=keyboard
            )

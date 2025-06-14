
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from collections import defaultdict

# Языковые подписи
BUTTON_LABELS = {
    "ru": {
        "next": "Далее ▶️",
        "back": "◀️ Назад",
        "menu": "Назад в меню ⏪",
    },
    "en": {
        "next": "Next ▶️",
        "back": "◀️ Back",
        "menu": "⬅️ Back to menu",
    }
}

SLIDERS = {
    "hotel": [
        {
            "photo": "static/hotels.jpeg",
            "caption": "\u0413\u043e\u0441\u0442\u0438\u043d\u0438\u0446\u0430 \u21161\n\u0420\u044f\u0434\u043e\u043c \u0441 \u0446\u0435\u043d\u0442\u0440\u043e\u043c"
        },
        {
            "photo": "static/amir-hotel.jpg",
            "caption": "\u0413\u043e\u0441\u0442\u0438\u043d\u0438\u0446\u0430 \u21162\n\u0421 \u0432\u0438\u0434\u043e\u043c \u043d\u0430 \u043e\u0437\u0435\u0440\u043e"
        },
        {
            "photo": "static/karagat-hotel.jpg",
            "caption": "\u0413\u043e\u0441\u0442\u0438\u043d\u0438\u0446\u0430 \u21163\n\u0421 \u0437\u0430\u0432\u0442\u0440\u0430\u043a\u043e\u043c"
        }
    ],
    "guest": [
        {
            "photo": "static/gueshouseeles.jpg",
            "caption": "\u0413\u043e\u0441\u0442\u0435\u0432\u043e\u0439 \u0434\u043e\u043c \u0410\u043d\u0430\u0440"
        },
        {
            "photo": "static/guest_house.jpg",
            "caption": "\u0413\u043e\u0441\u0442\u0435\u0432\u043e\u0439 \u0434\u043e\u043c \u041c\u044d\u044d\u0440\u0438\u043c"
        }
    ],
    "hostel": [
        {
            "photo": "static/showleopardHostel.webp",
            "caption": "\u0425\u043e\u0441\u0442\u0435\u043b Smile"
        },
        {
            "photo": "static/duetHostel.webp",
            "caption": "\u0425\u043e\u0441\u0442\u0435\u043b Family"
        }
    ],
    "cafe": [
        {
            "photo": "static/arinKafe.jpg",
            "caption": "\u041a\u0430\u0444\u0435 \u0443 \u041f\u0430\u043f\u044b"
        },
        {
            "photo": "static/altynkumaraKafe.jpg",
            "caption": "\u041a\u0430\u0444\u0435 \u0412\u043e\u0441\u0442\u043e\u0447\u043d\u043e\u0435"
        }
    ],
    "coffee": [
        {
            "photo": "static/foodKafe.jpg",
            "caption": "\u041a\u043e\u0444\u0435\u0439\u043d\u044f Karakol Coffee"
        },
        {
            "photo": "static/sierraCoffee.jpg",
            "caption": "\u041a\u043e\u0444\u0435\u0439\u043d\u044f Arabica"
        }
    ],
    "ashlyan": [
        {
            "photo": "static/ashlianfuгKafe.jpg",
            "caption": "\u0410\u0448\u043b\u044f\u043d\u0444\u0443 \u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439"
        },
        {
            "photo": "static/ashlianySaidyfuKafe.jpg",
            "caption": "\u0410\u0448\u043b\u044f\u043d\u0444\u0443 \u0432 \u0447\u0430\u0448\u043a\u0435"
        }
    ],
    "tour": [
        {
            "photo": "static/kayakingTour.jpg",
            "caption": "\u041f\u043e\u0435\u0437\u0434\u043a\u0430 \u043d\u0430 \u0414\u0436\u0435\u0442\u0438-\u041e\u0433\u0443\u0437"
        },
        {
            "photo": "static/skytour.jpg",
            "caption": "\u041f\u0435\u0448\u0438\u0439 \u0442\u0443\u0440 \u043f\u043e \u0443\u0449\u0435\u043b\u044c\u044e"
        }
    ],
    "sight": [
        {
            "photo": "static/museum.jpg",
            "caption": "\u041c\u0435\u0447\u0435\u0442\u044c \u0414\u0443\u0433\u0430\u043d\u0441\u043a\u0430\u044f"
        },
        {
            "photo": "static/mermalnyimusei.jpg",
            "caption": "\u0426\u0435\u0440\u043a\u043e\u0432\u044c \u0421\u0432\u044f\u0442\u043e\u0439 \u0422\u0440\u043e\u0438\u0446\u044b"
        }
    ]
}
user_last_photo_ids = defaultdict(list)

def clear_photos(bot, call):
    if user_last_photo_ids.get(call.message.chat.id):
        for msg_id in user_last_photo_ids[call.message.chat.id]:
            try:
                bot.delete_message(call.message.chat.id, msg_id)
            except:
                pass
        user_last_photo_ids[call.message.chat.id] = []

# ✅ Добавим параметр lang
def get_slider_buttons(index, category, lang="ru"):
    total = len(SLIDERS[category])
    keyboard = InlineKeyboardMarkup()
    labels = BUTTON_LABELS[lang]

    buttons = []
    if index > 0:
        buttons.append(InlineKeyboardButton(labels["back"], callback_data=f"{category}_{index - 1}"))
    if index < total - 1:
        buttons.append(InlineKeyboardButton(labels["next"], callback_data=f"{category}_{index + 1}"))

    if buttons:
        keyboard.row(*buttons)
    keyboard.add(InlineKeyboardButton(labels["menu"],
                                      callback_data="mainmenuenglish" if lang == "en" else "mainmenu"))
    return keyboard

def send_slider(bot, call, category, lang="ru"):
    # Определим язык
    lang = "en" if "en" in call.data or "english" in call.data else "ru"
    clear_photos(bot, call)
    index = 0
    slide = SLIDERS[category][index]
    with open(slide["photo"], "rb") as photo:
        msg = bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=slide["caption"],
            reply_markup=get_slider_buttons(index, category, lang)
        )
        user_last_photo_ids[call.message.chat.id].append(msg.message_id)

def edit_slider(bot, call, category, index, lang="ru"):
    lang = "en" if "en" in call.data or "english" in call.data else "ru"
    slide = SLIDERS[category][index]
    with open(slide["photo"], "rb") as photo:
        media = InputMediaPhoto(photo, caption=slide["caption"])
        bot.edit_message_media(
            media=media,
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=get_slider_buttons(index, category, lang)
        )
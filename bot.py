from email import message
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    button11 = types.InlineKeyboardButton(text="Русский", callback_data="button11")
    button22 = types.InlineKeyboardButton(text="English", callback_data="button22")
    keyboard.add(button11)
    keyboard.add(button22)

    bot.send_message(message.chat.id, text = "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот - Путеводитель. Выбери, то что тебя  интересует".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup = keyboard )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    kb = types.InlineKeyboardMarkup()  
    if call.message:
# Программа     
    #russion
        if call.data == "button11":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text="Туры", callback_data="button1")
            button2 = types.InlineKeyboardButton(text="Достопримечательности", callback_data="button2")
            button3 = types.InlineKeyboardButton(text="Отели", callback_data="button3")
            button4 = types.InlineKeyboardButton(text="Кафе", callback_data="button4")
            keyboard.add(button1)
            keyboard.add(button2)
            keyboard.add(button3)
            keyboard.add(button4)
            bot.send_message(call.message.chat.id, text="Меню",reply_markup=keyboard) 
    #english
        if call.data == "button22":
            keyboard = types.InlineKeyboardMarkup()
            button1en = types.InlineKeyboardButton(text="Tour", callback_data="button1en")
            button2en = types.InlineKeyboardButton(text="Attractives", callback_data="button2en")
            button3en = types.InlineKeyboardButton(text="Hotels", callback_data="button3en")
            button4en = types.InlineKeyboardButton(text="Cafe", callback_data="button4en")
            keyboard.add(button1en)
            keyboard.add(button2en)
            keyboard.add(button3en)
            keyboard.add(button4en)
            bot.send_message(call.message.chat.id, text="Menu",reply_markup=keyboard) 
            
        #menuRus
        if call.data == "mainmenu":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text="Туры", callback_data="button1")
            button2 = types.InlineKeyboardButton(text="Достопримечательности", callback_data="button2")
            button3 = types.InlineKeyboardButton(text="Отели", callback_data="button3")
            button4 = types.InlineKeyboardButton(text="Кафе", callback_data="button4")
            keyboard.add(button1)
            keyboard.add(button2)
            keyboard.add(button3)
            keyboard.add(button4)
            bot.send_message(call.message.chat.id, text="Меню",reply_markup=keyboard)

   #menuEngl
        if call.data == "mainmenuenglish":
            keyboard = types.InlineKeyboardMarkup()
            button1en = types.InlineKeyboardButton(text="Tours", callback_data="button1en")
            button2en = types.InlineKeyboardButton(text="Attractives", callback_data="button2en")
            button3en = types.InlineKeyboardButton(text="Hotels", callback_data="button3en")
            button4en = types.InlineKeyboardButton(text="Cafe", callback_data="button4en")
            keyboard.add(button1en)
            keyboard.add(button2en)
            keyboard.add(button3en)
            keyboard.add(button4en)
            bot.send_message(call.message.chat.id, text="Меню",reply_markup=keyboard)

        if call.data == "button1":
            kb.add(
                types.InlineKeyboardButton(text="Культурные туры", callback_data="tur0")
            )
            kb.add(
                types.InlineKeyboardButton(text="Горные туры/Тарекинг🌄", callback_data="tur1"),
                types.InlineKeyboardButton(text="Конные туры🐎", callback_data="tur2")
            )
            kb.add(
                types.InlineKeyboardButton(text="Лыжные туры🎿", callback_data="tur3"),
                types.InlineKeyboardButton(text="Авто туры🚗", callback_data="tur4")
            )
            kb.add(
                types.InlineKeyboardButton(text="Каякинг⛵", callback_data="tur6")
            )
            kb.add(
                types.InlineKeyboardButton(text="Велотур🚴‍♂️", callback_data="tur7"),
                
            )
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Виды туров", reply_markup=kb)
    #en
        if call.data == "button1en":
            kb.add(
                types.InlineKeyboardButton(text="Cultural tours", callback_data="tur0")
            )
            kb.add(
                types.InlineKeyboardButton(text="Hiking🌄", callback_data="tur1"),
                types.InlineKeyboardButton(text="Hourse riding🐎", callback_data="tur2")
            )
            kb.add(
                types.InlineKeyboardButton(text="Ski tours🎿", callback_data="tur3"),
                types.InlineKeyboardButton(text="Auto tours🚗", callback_data="tur4")
            )
            kb.add(
                types.InlineKeyboardButton(text="Kayaking⛵", callback_data="tur6")
            )
            kb.add(
                types.InlineKeyboardButton(text="Cycling tours 🚴‍♂️", callback_data="tur7"),
                
            )
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            bot.send_message(call.message.chat.id, "Types of tours", reply_markup=kb)

  

        if call.data == "button2":
            kb.add(types.InlineKeyboardButton(text="Собор Святой Троицы - церковь🛕", callback_data="dost1"))
            kb.add(types.InlineKeyboardButton(text="Дунганская мечеть🕌", callback_data="dost2"))
            kb.add(types.InlineKeyboardButton(text="Исторический музей г.Каракол", callback_data="dost5"))
            kb.add(types.InlineKeyboardButton(text="Мемориальный музей Н.М.Пржевальского", callback_data="dost6"))
            kb.add(types.InlineKeyboardButton(text="Еще больше достопримечательностей➕", url="https://www.ski-karakol.com/karakol/dostoprimechatel6nosti.aspx"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))

            bot.send_message(call.message.chat.id, "Виды Достопримечательностей", reply_markup=kb)

#en
        if call.data == "button2en":
            kb.add(types.InlineKeyboardButton(text="Holy trinity cathedral🛕", callback_data="dost1en"))
            kb.add(types.InlineKeyboardButton(text="Dungan mosque🕌", callback_data="dost2en"))
            kb.add(types.InlineKeyboardButton(text="Historical museum ", callback_data="dost5en"))
            kb.add(types.InlineKeyboardButton(text="Przhewalski museum", callback_data="dost6en"))
            kb.add(types.InlineKeyboardButton(text="More attactions➕", url="https://www.ski-karakol.com/karakol/dostoprimechatel6nosti.aspx"))
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))

            bot.send_message(call.message.chat.id, "Types of attractions", reply_markup=kb)

        if call.data == "button3":
            kb.add(
                types.InlineKeyboardButton(text="Отели", callback_data="hotel1"),
                types.InlineKeyboardButton(text="Гостевые Дома", callback_data="hotel2")
            )
            kb.add(
                types.InlineKeyboardButton(text="Хостелы", callback_data="hotel3"),
                types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu")
            )

            bot.send_message(call.message.chat.id, "Переночевать😴?", reply_markup=kb)

#en
        if call.data == "button3en":
            kb.add(
                types.InlineKeyboardButton(text="Hotels", callback_data="hotel1en"),
                types.InlineKeyboardButton(text="Guest house", callback_data="hotel2en")
            )
            kb.add(
                types.InlineKeyboardButton(text="Hostels", callback_data="hotel3en"),
                types.InlineKeyboardButton(text="Back to menue⏪", callback_data="mainmenuenglish")
            )

            bot.send_message(call.message.chat.id, "stay overnight😴?", reply_markup=kb)



        if call.data == "button4":
            kb.add(types.InlineKeyboardButton(text="Кафе", callback_data="kafe1"))
            kb.add(types.InlineKeyboardButton(text="Кафейня", callback_data="kafe2"))
            kb.add(types.InlineKeyboardButton(text="Ашлянфу", callback_data="kafe3"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))

            bot.send_message(call.message.chat.id, "Где поесть😋?", reply_markup=kb)

#en
        if call.data == "button4en":
            kb.add(types.InlineKeyboardButton(text="Cafe", callback_data="kafe1en"))
            kb.add(types.InlineKeyboardButton(text="Coffee shop", callback_data="kafe2en"))
            kb.add(types.InlineKeyboardButton(text="Dungan ashlan fu", callback_data="kafe3en"))
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))

            bot.send_message(call.message.chat.id, "Where to eat in Karakol😋?", reply_markup=kb)



# Под программа ТУРЫ

        #КУЛЬТУРНЫЕ ТУРЫ
        af = types.InlineKeyboardMarkup()  
        aff = types.InlineKeyboardMarkup()  
        if call.data == "tur0":
            af.add(types.InlineKeyboardButton(text="Visit Karakol", callback_data="culturetourvisit"))
            af.add(types.InlineKeyboardButton(text="ECOTREK", callback_data="culturetoureco"))
            af.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>Культурные</b> туры:", parse_mode='html', reply_markup=af)

        if call.data == 'culturetourvisit':
            aff.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/nomads_way"))
            aff.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            photo = open('static/cultureTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Этот тур создан для людей, которые заинтересованы в знакомстве с основными достопримечательностями, культурой и любят делать удивительные фотографии живописных пейзажей без больших физических нагрузок. Подробности про тур вы можете узнать на сайте",  reply_markup=aff)

        if call.data == 'culturetoureco':
            aff.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/nomads_way"))
            aff.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            photo = open('static/ecotrekTour1.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "В этом туре вы познакомитесь с культурой, традициями и бытом кочевников, бытом и развлечениями крупных городов, а также посетите живописные природные места, которыми славится Кыргызстан. Верховая езда, покорение горных вершин, пикники и охота, а также пляжный отдых на берегу озера Иссык-Куль – все это входит в программы кыргызского культурного тура. Подробности про тур вы можете узнать на сайте", reply_markup=aff)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))

        #ГОРНЫЕ ТУРЫ
        ae = types.InlineKeyboardMarkup()  
        aee = types.InlineKeyboardMarkup()  
        if call.data == "tur1":
            ae.add(types.InlineKeyboardButton(text="Bulak Say", callback_data="trekkingtour"))
            ae.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>горные</b> туры:", parse_mode='html', reply_markup=ae)

        if call.data == 'trekkingtour':
            aee.add(types.InlineKeyboardButton(text="Сайт", url="http://karakoltour.kg/index.php/ru/kayaking"))
            aee.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            photo = open('static/horsebackTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Bulak Say Horseback and Trekking — это семейный туроператор, базирующийся в селе Жолголот, недалеко от города горных походов Каракол. Наша конная база расположена у подножия пастбища между Караколом и хребтом Терскей Ала-Тоо в 10 минутах езды на такси от центра города. Мы предлагаем конные и пешие туры от 1 до 10 дней по красивым долинам и перевалам Тянь-Шаня и ночевки в юртах с традиционной кыргызской едой и свежими молочными продуктами с нашей фермы.", parse_mode='html', reply_markup=aee)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #Конные туры
        ad = types.InlineKeyboardMarkup()  
        add = types.InlineKeyboardMarkup()  
        if call.data == "tur2":
            ad.add(types.InlineKeyboardButton(text="Bulak Say", callback_data="horsbacktour"))
            ad.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают туры<b>верховых езд:</b> ", parse_mode='html', reply_markup=ad)

        if call.data == 'horsbacktour':
            add.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/"))
            photo = open('static/horsebackTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Bulak Say Horseback and Trekking — это семейный туроператор, базирующийся в селе Жолголот, недалеко от города горных походов Каракол. Наша конная база расположена у подножия пастбища между Караколом и хребтом Терскей Ала-Тоо в 10 минутах езды на такси от центра города. Мы предлагаем конные и пешие туры от 1 до 10 дней по красивым долинам и перевалам Тянь-Шаня и ночевки в юртах с традиционной кыргызской едой и свежими молочными продуктами с нашей фермы. Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=add)

            add.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #Лыжные ТУРЫ
        aj = types.InlineKeyboardMarkup()  
        ajj = types.InlineKeyboardMarkup()  
        if call.data == "tur3":
            aj.add(types.InlineKeyboardButton(text="VISIT KARAKOL ", callback_data="skitour"))
            aj.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>Лыжные</b> туры:", parse_mode='html', reply_markup=aj)

        if call.data == 'skitour':
            ajj.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/freeride_and_ski_tours_in_kyrgyzstan"))
            photo = open('static/skytour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Здесь у вас будет возможность отлично провести время, занимаясь фрирайдом и скитуром по Кыргызстану. Наши снежные горы относятся к горам Тянь-Шаня, географически обособленной стране с хорошо сохранившейся кочевой культурой. Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=ajj)

            ajj.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #АВТО ТУР
        ac = types.InlineKeyboardMarkup()  
        acc = types.InlineKeyboardMarkup()  
        if call.data == "tur4":
            ac.add(types.InlineKeyboardButton(text="VISIT KARAKOL", callback_data="avtotur"))
            ac.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>авто</b> туры:", parse_mode='html', reply_markup=ac)

        if call.data == 'avtotur':
            acc.add(types.InlineKeyboardButton(text="Сайт", url="http://karakoltour.kg/index.php/ru/kayaking"))
            photo = open('static/avtoTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Мы рассказываем о Караколе, Кыргызстане все, что вы хотите знать! Взгляните на страну глазами туристов и самих жителей! Это идеальное место для внедорожных туров с посещением живописных ущелий и каньонов, долин и рек, гор и озер! Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=acc)

            acc.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #КАЯККИНГ
        ab = types.InlineKeyboardMarkup()  
        abb = types.InlineKeyboardMarkup()  
        if call.data == "tur6":
            ab.add(types.InlineKeyboardButton(text="Issyk-Kul Kayaking", callback_data="kayaking"))
            ab.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>каяккинг</b> туры: ", parse_mode='html', reply_markup=ab)

        if call.data == 'kayaking':
            abb.add(types.InlineKeyboardButton(text="Сайт", url="http://karakolhorsetrekking.blogspot.com/"))
            abb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            photo = open('static/kayakingTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Каякинг тур по озеру Иссык-Куль Предлагаем каякинг тур по озеру Иссык-Куль продолжительностью до 5 часов. Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=abb)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #ВЕЛОТУР 
        ah = types.InlineKeyboardMarkup() 
        if call.data == "tur7":
            ah.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Пока что в разделе 'Велотур' отсуствует туры", reply_markup=ah)



# Под программа ДОСТОПРИМЕЧАТЕЛЬНОСТЕЙ
        if call.data == "dost1":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/AHY9ZdA2nUJeDayMA"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/karakolcathedral.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Свято-Троицкая православная церковь🛕.  Это сооружение – классический пример Русской Православной Церкви XIX века. Изящное здание с деревянными стенами и причудливым орнаментом прочно стоит на каменном фундаменте. Пять золотых куполов украшают крышу Собора, внутри которого находится множество икон, в том числе и копия иконы Андрея Рублева «Святая Троица».", reply_markup=kb)

#en
        if call.data == "dost1en":
            kb.add(types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/AHY9ZdA2nUJeDayMA"))
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/karakolcathedral.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Holy Trinity Orthodox Church🛕.  This structure is a classic example of the Russian Orthodox Church of the 19th century. The elegant building with wooden walls and fanciful ornamentation stands firmly on a stone foundation. Five golden domes adorn the roof of the cathedral, and inside there are many icons, including a copy of Andrei Rublev's 'Holy Trinity'icon».", reply_markup=kb)


        if call.data == "dost2":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/fGuhF9crif9WYCyq9"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/karakoldunganmosque.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Дунганская мечеть🕌 - одна из самых интересных достопримечательностей города Каракол. Дизайн и проект мечети выдержаны согласно принципам китайской архитектуры времен империи Цин. Мечеть без единого гвоздя", reply_markup=kb)

#en
        if call.data == "dost2en":
            kb.add(types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/fGuhF9crif9WYCyq9"))
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/karakoldunganmosque.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "The Dungan Mosque🕌 is one of the most interesting sights in Karakol. The design and the project of the mosque are based on the principles of Chinese architecture of the Qing Empire. Mosque without a single nail", reply_markup=kb)


        if call.data == "dost5":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/ceYRFM4w3FJV16UA7"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/museum.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Каракольский историко-краеведческий музей был основан в 1948 году. Экспонаты музея отражают историю развития края, его природные богатства, развитие промышленности, сельского хозяйства, культуры, образования, здравоохранения и рассказывают об известных людях области.", reply_markup=kb)

#en
        if call.data == "dost5en":
            kb.add(types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/ceYRFM4w3FJV16UA7"))
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/museum.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Karakol History and Local History Museum was founded in 1948. Exhibits of the museum reflect the history of the development of the region, its natural resources, the development of industry, agriculture, culture, education, health, and tell about famous people of the region.", reply_markup=kb)

        if call.data == "dost6":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/6CHQKMpCD6BovG286"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/mermalnyimusei.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Главной достопримечательностью Каракола конечно же является парк-заповедник с могилой и мемориалом Н.М.Пржевальского . В 9 км к северу от города, недалеко от пристани в Каракольском заливе среди парка находятся музей, памятник и могила Н. М. Пржевальского. На пути в свое 5-е путешествие Пржевальский умирает в городе Каракол и по его желанию он похоронен на берегу Иссык-Куля. Он находится на самой высокой точке восточной части Иссык-Кульского побережья. Так что вид отсюда открывается просто необыкновенный: величественная панорама озера и голубые шапки гор. Как бы охраняя вход в парк, по бокам ворот на высоких постаментах застыли козероги-тэке", reply_markup=kb)

#en
        if call.data == "dost6en":
            kb.add(types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/6CHQKMpCD6BovG286"))
            kb.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/mermalnyimusei.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "The main attraction of Karakol, of course, is the park-reserve with the tomb and memorial of N.M. Przhevalsky. N. M. Przhevalsky's museum, monument and grave are located 9 km to the north of the town, not far from the pier in Karakol Bay among the park. On his way to his 5th journey, Przhevalsky died in the town of Karakol and was buried at his wish on the shore of Issyk Kul. It is located on the highest point of the eastern part of the Issyk-Kul coast. So, the view from here is simply extraordinary: the majestic panorama of the lake and the blue caps of the mountains. As if guarding the entrance to the park, the ibex-taike-goats stand on high pedestals on the sides of the gates", reply_markup=kb)





# Под программа Отели    
        if call.data == "hotel1":
             #1
            kk = types.InlineKeyboardMarkup()
            kk.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/REUP3jyqLVLpy22K8"),
                types.InlineKeyboardButton(text="Бронирование", url="https://karagat-hotel-karakol.nochi.com/")
            )
            photo = open('static/karagat-hotel.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Карагат",parse_mode='html', reply_markup=kk)

            #2
            ll = types.InlineKeyboardMarkup()

            ll.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/aYhP5k9dQhwCK3cQA"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.booking.com/hotel/kg/dd1-4d-n.ru.html?aid=318615&label=Russian_Kyrgyzstan_RU_KG_29377901185-_LNFadyyFJxSoSSqNZCUlQS111450060385%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi10638584468%3Atiaud-294889297133%3Adsa-320367708406%3Alp9070442%3Ali%3Adec%3Adm&sid=f173aeeb6b0ef9b7a21bba06597de56d&dest_id=-2331996;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1650787367;srpvid=ad5a3893cdd500f9;type=total;ucfs=1&#hotelTmpl")
            )

            photo = open('static/amir-hotel.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>2)</b>Амир",parse_mode='html', reply_markup=ll)

            #3
            mm = types.InlineKeyboardMarkup()
            mm.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.booking.com/city/kg/karakol.ru.html?aid=319915;label=karakol-nsIDLr0ukzAYECiYwmobWgS275096107816:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-39720801976:lp9070442:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU;ws=&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fJZ2p28EMP5Kb4YUk9rXgp35NrKvEPBCMn2hqqn6ODDm9yHw-AG-ZcaAsBkEALw_wcB"))
            mm.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/hotels.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Отелей по ссылке👇",parse_mode='html', reply_markup=mm)



#en
        if call.data == "hotel1en":
            #1
            kk = types.InlineKeyboardMarkup()
            kk.add(
                types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/REUP3jyqLVLpy22K8"),
                types.InlineKeyboardButton(text="Booking", url="https://karagat-hotel-karakol.nochi.com/")
            )
            photo = open('static/karagat-hotel.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Karagat",parse_mode='html', reply_markup=kk)

            #2
            ll = types.InlineKeyboardMarkup()

            ll.add(
                types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/aYhP5k9dQhwCK3cQA"),
                types.InlineKeyboardButton(text="Booking", url="https://www.booking.com/hotel/kg/dd1-4d-n.ru.html?aid=318615&label=Russian_Kyrgyzstan_RU_KG_29377901185-_LNFadyyFJxSoSSqNZCUlQS111450060385%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi10638584468%3Atiaud-294889297133%3Adsa-320367708406%3Alp9070442%3Ali%3Adec%3Adm&sid=f173aeeb6b0ef9b7a21bba06597de56d&dest_id=-2331996;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1650787367;srpvid=ad5a3893cdd500f9;type=total;ucfs=1&#hotelTmpl")
            )

            photo = open('static/amir-hotel.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>2)</b>Amir",parse_mode='html', reply_markup=ll)

            #3
            mm = types.InlineKeyboardMarkup()
            mm.add(types.InlineKeyboardButton(text="Link", url="https://www.booking.com/city/kg/karakol.ru.html?aid=319915;label=karakol-nsIDLr0ukzAYECiYwmobWgS275096107816:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-39720801976:lp9070442:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU;ws=&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fJZ2p28EMP5Kb4YUk9rXgp35NrKvEPBCMn2hqqn6ODDm9yHw-AG-ZcaAsBkEALw_wcB"))
            mm.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenu"))
            
            photo = open('static/hotels.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "To find more hotels follow the link👇",parse_mode='html', reply_markup=mm)



# Под программа Гостевой Дом    
        if call.data == "hotel2":
            #1
            nn = types.InlineKeyboardMarkup()
            nn.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/hotel-altai-kg?share"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.booking.com/hotel/kg/guest-house-altay.ru.html?aid=315714&label=guest-house-altay-PntHSJ7WT4xWLwJVVPgLeQS442453470933%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-180775626966%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YQB9rNbOPxnnhY6p2cOLx0E&sid=f173aeeb6b0ef9b7a21bba06597de56d&dest_id=-2331996;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1650787955;srpvid=6f7c39b8c6500068;type=total;ucfs=1&#hotelTmpl")
            )
            photo = open('static/altay-guesthouse.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Гостевой Дом Altay",parse_mode='html', reply_markup=nn)

            #2
            oo = types.InlineKeyboardMarkup()
            oo.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/aYhP5k9dQhwCK3cQA"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.booking.com/hotel/kg/tikhii-ugholok.ru.html?aid=1149971&label=karakol-PPCTJg56Fs1W3eKyi%2A9UIgS390176536984%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565747%3Akwd-66950393424%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz10S2LDvGAHUOI&sid=f173aeeb6b0ef9b7a21bba06597de56d")
            )
            photo = open('static/gueshouseeles.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Гостевой Дом Eles",parse_mode='html', reply_markup=oo)


#en
        if call.data == "hotel2en":
            #1
            nn = types.InlineKeyboardMarkup()
            nn.add(
                types.InlineKeyboardButton(text="Link to map", url="https://g.page/hotel-altai-kg?share"),
                types.InlineKeyboardButton(text="Booking", url="https://www.booking.com/hotel/kg/guest-house-altay.ru.html?aid=315714&label=guest-house-altay-PntHSJ7WT4xWLwJVVPgLeQS442453470933%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-180775626966%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YQB9rNbOPxnnhY6p2cOLx0E&sid=f173aeeb6b0ef9b7a21bba06597de56d&dest_id=-2331996;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1650787955;srpvid=6f7c39b8c6500068;type=total;ucfs=1&#hotelTmpl")
            )
            photo = open('static/altay-guesthouse.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Guest house Altay",parse_mode='html', reply_markup=nn)

            #2
            oo = types.InlineKeyboardMarkup()
            oo.add(
                types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/aYhP5k9dQhwCK3cQA"),
                types.InlineKeyboardButton(text="Booking", url="https://www.booking.com/hotel/kg/tikhii-ugholok.ru.html?aid=1149971&label=karakol-PPCTJg56Fs1W3eKyi%2A9UIgS390176536984%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565747%3Akwd-66950393424%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz10S2LDvGAHUOI&sid=f173aeeb6b0ef9b7a21bba06597de56d")
            )
            photo = open('static/gueshouseeles.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Guest house Eles",parse_mode='html', reply_markup=oo)

            #3
            mm = types.InlineKeyboardMarkup()
            mm.add(types.InlineKeyboardButton(text="Link", url="https://www.booking.com/guest-house/city/kg/karakol.ru.html?aid=1149971&label=karakol-PPCTJg56Fs1W3eKyi%2A9UIgS390176536984%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565747%3Akwd-66950393424%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz10S2LDvGAHUOI&sid=f173aeeb6b0ef9b7a21bba06597de56d&keep_landing=1&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fLIEDEbnC2BNuqenj1QivuwpYkHl6DWvLMte56tOh48-OCwUp3oBQgaAgK2EALw_wcB&"))
            mm.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/guest_house.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "More guest house by link👇",parse_mode='html', reply_markup=mm)

            



# Под программа Хостелы   
        if call.data == "hotel3":
            #1
            pp = types.InlineKeyboardMarkup()
            pp.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/duethostel?share"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.russian.hostelworld.com/hosteldetails.php/Snow-Leopard-Hostel/Karakol/299894")
            )
            photo = open('static/showleopardHostel.webp', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Хостел Snow Leopard", parse_mode='html', reply_markup=pp)

            #2
            qq = types.InlineKeyboardMarkup()
            qq.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/duethostel?share"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.russian.hostelworld.com/hosteldetails.php/Duet-Hostel/Karakol/272558")
            )

            photo = open('static/duetHostel.webp', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Duet hostel",parse_mode='html', reply_markup=qq)

            #3
            rr = types.InlineKeyboardMarkup()
            rr.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.russian.hostelworld.com/khostely/Karakol/Kirgizia?source=ppc_gooads_nonbrand_dsk_search_ds_ru_row&network=g&campaign_id=15296631596&adgroup_id=128648200054&criteria_id=kwd-844803786662&creative_id=571201068429&location_physical_id=9070442&location_interest_id=&adposition=&uniqueclickID=1270539567961807976&sub_keyword=hostel%2520karakol&sub_ad=e&sub_publisher=ADW&gclsrc=aw.ds&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fKr6vpeJVQR3pbJE7FRUXLQoudQ0je6jvtloGOWqjzh-Bu4fh-5tCMaAgmfEALw_wcB")),
            rr.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/guest_house.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Хостелов по ссылке👇",parse_mode='html', reply_markup=rr)

#en
        if call.data == "hotel3en":
            #1
            pp = types.InlineKeyboardMarkup()
            pp.add(
                types.InlineKeyboardButton(text="Link to map", url="https://g.page/duethostel?share"),
                types.InlineKeyboardButton(text="Booking", url="https://www.russian.hostelworld.com/hosteldetails.php/Snow-Leopard-Hostel/Karakol/299894")
            )
            photo = open('static/showleopardHostel.webp', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Hostel Snow Leopard", parse_mode='html', reply_markup=pp)

            #2
            qq = types.InlineKeyboardMarkup()
            qq.add(
                types.InlineKeyboardButton(text="Link to map", url="https://g.page/duethostel?share"),
                types.InlineKeyboardButton(text="Booking", url="https://www.russian.hostelworld.com/hosteldetails.php/Duet-Hostel/Karakol/272558")
            )

            photo = open('static/duetHostel.webp', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Duet hostel",parse_mode='html', reply_markup=qq)

            #3
            rr = types.InlineKeyboardMarkup()
            rr.add(types.InlineKeyboardButton(text="Link", url="https://www.russian.hostelworld.com/khostely/Karakol/Kirgizia?source=ppc_gooads_nonbrand_dsk_search_ds_ru_row&network=g&campaign_id=15296631596&adgroup_id=128648200054&criteria_id=kwd-844803786662&creative_id=571201068429&location_physical_id=9070442&location_interest_id=&adposition=&uniqueclickID=1270539567961807976&sub_keyword=hostel%2520karakol&sub_ad=e&sub_publisher=ADW&gclsrc=aw.ds&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fKr6vpeJVQR3pbJE7FRUXLQoudQ0je6jvtloGOWqjzh-Bu4fh-5tCMaAgmfEALw_wcB")),
            rr.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/guest_house.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "More hostels by link👇",parse_mode='html', reply_markup=rr)



# Под программа КАФЕЩЕК: Кафе
        if call.data == "kafe1":
            #1
            kb.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/WmqDi9pM4Mca4jX67"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/ShowUserReviews-g815340-d3952646-r190813567-Cafe_Zarina-Karakol_Issyk_Kul_Province.html")
            )
            kb.add(
                types.InlineKeyboardButton(text="Меню", url="https://media-cdn.tripadvisor.com/media/photo-s/10/16/df/c6/cafe-zarina.jpg")
            )
            
            photo = open('static/zarinKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b> кафе Зарина",parse_mode='html', reply_markup=kb)

            #2
            aa = types.InlineKeyboardMarkup()
            photo = open('static/altynkumaraKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            aa.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/n2aZ2Bi7NkE88fLm6"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d13313936-Reviews-Altyn_Kumara-Karakol_Issyk_Kul_Province.html")
            )
            aa.add(
                types.InlineKeyboardButton(text="Меню", url="https://www.instagram.com/stories/highlights/17903538839038951/")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b> кафе Алтын Кумара",parse_mode='html', reply_markup=aa)

            #3
            bb = types.InlineKeyboardMarkup()
            bb.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/cafe_dastorkon?share"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d6481971-Reviews-Ethnic_Cafe_Dastorkon-Karakol_Issyk_Kul_Province.html")
            )
            bb.add(
                types.InlineKeyboardButton(text="Меню", url="https://www.instagram.com/stories/highlights/17882963158335616/")
            )
            
            photo = open('static/dastarkonKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>3)</b> кафе Дастаркон",parse_mode='html', reply_markup=bb)

            #4
            cc = types.InlineKeyboardMarkup()
            cc.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%BA%D0%B0%D1%84%D0%B5&searchSessionId=496BF566B033821C632CE1B21ED455D41650760078349ssid&searchNearby=false&geo=815340&sid=D0B03FB321A0422180BFF0D3F6956E3A1650760305616&blockRedirect=true"))
            cc.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/foodKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше кафе по ссылке👇",parse_mode='html', reply_markup=cc)     


#en
        if call.data == "kafe1en":
            #1
            kb.add(
                types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/WmqDi9pM4Mca4jX67"),
                types.InlineKeyboardButton(text="Link to site", url="https://www.tripadvisor.ru/ShowUserReviews-g815340-d3952646-r190813567-Cafe_Zarina-Karakol_Issyk_Kul_Province.html")
            )
            kb.add(
                types.InlineKeyboardButton(text="Menu", url="https://media-cdn.tripadvisor.com/media/photo-s/10/16/df/c6/cafe-zarina.jpg")
            )
            
            photo = open('static/zarinKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Cofe Zarina",parse_mode='html', reply_markup=kb)

            #2
            aa = types.InlineKeyboardMarkup()
            photo = open('static/altynkumaraKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            aa.add(
                types.InlineKeyboardButton(text="Link to map", url="https://goo.gl/maps/n2aZ2Bi7NkE88fLm6"),
                types.InlineKeyboardButton(text="Link to site", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d13313936-Reviews-Altyn_Kumara-Karakol_Issyk_Kul_Province.html")
            )
            aa.add(
                types.InlineKeyboardButton(text="Menu", url="https://www.instagram.com/stories/highlights/17903538839038951/")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b>Cafe Altyn-Kumara",parse_mode='html', reply_markup=aa)

            #3
            bb = types.InlineKeyboardMarkup()
            bb.add(
                types.InlineKeyboardButton(text="Link to map", url="https://g.page/cafe_dastorkon?share"),
                types.InlineKeyboardButton(text="Link to site", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d6481971-Reviews-Ethnic_Cafe_Dastorkon-Karakol_Issyk_Kul_Province.html")
            )
            bb.add(
                types.InlineKeyboardButton(text="Menu", url="https://www.instagram.com/stories/highlights/17882963158335616/")
            )
            
            photo = open('static/dastarkonKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>3)</b>Cafe Dastarkon",parse_mode='html', reply_markup=bb)

            #4
            cc = types.InlineKeyboardMarkup()
            cc.add(types.InlineKeyboardButton(text="Link", url="https://www.tripadvisor.ru/Search?q=%D0%BA%D0%B0%D1%84%D0%B5&searchSessionId=496BF566B033821C632CE1B21ED455D41650760078349ssid&searchNearby=false&geo=815340&sid=D0B03FB321A0422180BFF0D3F6956E3A1650760305616&blockRedirect=true"))
            cc.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/foodKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "More cafe by link👇",parse_mode='html', reply_markup=cc) 

# Под программа КАФЕЩЕК: Кафейня
        if call.data == "kafe2":
            #1
            dd = types.InlineKeyboardMarkup()
            dd.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/sierra-coffee-karakol?share"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://sierra.madanur.com/")
            )
            photo = open('static/sierraCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b> Кофейня SIERRA Coffee Karakol",parse_mode='html', reply_markup=dd)

            #2
            ee = types.InlineKeyboardMarkup()
            photo = open('static/lighthouseCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            ee.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/QzDeWcYmWSyBegsK7"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d12941444-Reviews-Lighthouse_Coffee_Tea-Karakol_Issyk_Kul_Province.html")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b> Кофейня Karakol Lighthouse",parse_mode='html', reply_markup=ee)

            #3
            ff = types.InlineKeyboardMarkup()
            ff.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/meetingpoint-karakol?share"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://duetkarakol.wordpress.com/meeting-point/")
            )
            photo = open('static/meetingpointCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>3)</b> Кофейня Meeting Point",parse_mode='html', reply_markup=ff)

            #4
            gg = types.InlineKeyboardMarkup()
            gg.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D1%8F&searchSessionId=E1F43A879460082504B36AB7B431BD701650761090729ssid&searchNearby=false&geo=12257498&sid=D0B03FB321A0422180BFF0D3F6956E3A1650761097726&blockRedirect=true&rf=1"))
            gg.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/cupofcoffee.JPG', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Кофейни по ссылке👇",parse_mode='html', reply_markup=gg)    


#en
        if call.data == "kafe2en":
            #1
            dd = types.InlineKeyboardMarkup()
            dd.add(
                types.InlineKeyboardButton(text="Link to map", url="https://g.page/sierra-coffee-karakol?share"),
                types.InlineKeyboardButton(text="Link to site", url="https://sierra.madanur.com/")
            )
            photo = open('static/sierraCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b> Coffee shop SIERRA Coffee Karakol",parse_mode='html', reply_markup=dd)

            #2
            ee = types.InlineKeyboardMarkup()
            photo = open('static/lighthouseCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            ee.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/QzDeWcYmWSyBegsK7"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d12941444-Reviews-Lighthouse_Coffee_Tea-Karakol_Issyk_Kul_Province.html")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b> Coffee shop Karakol Lighthouse",parse_mode='html', reply_markup=ee)

            #3
            ff = types.InlineKeyboardMarkup()
            ff.add(
                types.InlineKeyboardButton(text="Link to map", url="https://g.page/meetingpoint-karakol?share"),
                types.InlineKeyboardButton(text="Link to site", url="https://duetkarakol.wordpress.com/meeting-point/")
            )
            photo = open('static/meetingpointCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>3)</b> Coffee shop Meeting Point",parse_mode='html', reply_markup=ff)

            #4
            gg = types.InlineKeyboardMarkup()
            gg.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D1%8F&searchSessionId=E1F43A879460082504B36AB7B431BD701650761090729ssid&searchNearby=false&geo=12257498&sid=D0B03FB321A0422180BFF0D3F6956E3A1650761097726&blockRedirect=true&rf=1"))
            gg.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/cupofcoffee.JPG', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "More link by link👇",parse_mode='html', reply_markup=gg)



# Под программа КАФЕЩЕК: Ашлянфу    
        if call.data == "kafe3":
            #1
            hh = types.InlineKeyboardMarkup()
            hh.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://go.2gis.com/qkr9f")
            )
            
            photo = open('static/ashlianySaidyfuKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Ашлянфу у Саиды",parse_mode='html', reply_markup=hh)

            #2
            ii = types.InlineKeyboardMarkup()
            photo = open('static/ashlianfuKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            ii.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://go.2gis.com/qkr9f")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b>Ашлянфу",parse_mode='html', reply_markup=ii)

            #3
            jj = types.InlineKeyboardMarkup()
            jj.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D1%8F&searchSessionId=E1F43A879460082504B36AB7B431BD701650761090729ssid&searchNearby=false&geo=12257498&sid=D0B03FB321A0422180BFF0D3F6956E3A1650761097726&blockRedirect=true&rf=1"))
            jj.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/ashlianfuгKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Ашлянфу по ссылке👇",parse_mode='html', reply_markup=jj) 


#en
        if call.data == "kafe3en":
            #1
            hh = types.InlineKeyboardMarkup()
            hh.add(
                types.InlineKeyboardButton(text="Link to map", url="https://go.2gis.com/qkr9f")
            )
            
            photo = open('static/ashlianySaidyfuKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Ashlian fu",parse_mode='html', reply_markup=hh)

            #2
            ii = types.InlineKeyboardMarkup()
            photo = open('static/ashlianfuKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            ii.add(
                types.InlineKeyboardButton(text="link to map", url="https://go.2gis.com/qkr9f")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b>Ashlan fu",parse_mode='html', reply_markup=ii)

            #3
            jj = types.InlineKeyboardMarkup()
            jj.add(types.InlineKeyboardButton(text="Link", url="https://www.tripadvisor.ru/Search?q=%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D1%8F&searchSessionId=E1F43A879460082504B36AB7B431BD701650761090729ssid&searchNearby=false&geo=12257498&sid=D0B03FB321A0422180BFF0D3F6956E3A1650761097726&blockRedirect=true&rf=1"))
            jj.add(types.InlineKeyboardButton(text="Back to menu⏪", callback_data="mainmenuenglish"))
            
            photo = open('static/ashlianfuгKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "More ashlan fu by link👇",parse_mode='html', reply_markup=jj) 


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, "Непонятное вырожение")   
    
bot.polling(none_stop=True)
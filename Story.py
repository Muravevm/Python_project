# Файл с сюжетным наполнением

# Массив с фонами
background_list = ["assets/Forest.png", "assets/Space.jpg", "assets/Hut.jpg", "assets/InHut.jpg", "assets/Village.jpg", "assets/Tavern.jpg"]

# Массив с музыкой
music_list = ["assets/hope.mp3"]

# Массив с картинками для кнопок
button_list = ["assets/Button.png", "assets/Button2.png"]

# Текста на первую кнопку
first_button_text = ["Встать на ноги", "Встать на ноги", "Встать на ноги", "Идти куда то", "Идти куда то", "Встать на ноги", "Встать на ноги",
                     "Идти куда то", "Идти прямо к крестьянам", "Заночевать в поле", "Подумать что делать дальше", "Зайти внутрь", "Искать еду", "Подумать что делать дальше",
                     "Идти куда глаза глядят", "Спать", "Съесть", "Снова искать выход из леса", "Зайти в первый же дом", "", "Остаться и обустроиться",
                     "Стать друидом и остаться здесь", "Искать выход", "Искать лучше", "Искать старосту", "Спросить, можно ли вам жить здесь",
                     "Выпить", "", "Идти в деревню", "", "", "Да не я это...", "", "", ""]

# Текста на вторую кнопку
second_button_text = ["Вспомнить как я здесь оказался", "Вспомнить как я здесь оказался", "Осмотреться", "3вать на помощь", "3вать на помощь",
                      "", "", "", "Идти вдоль кромки леса", "Искать более подходящее место", "", "Пройти мимо", "Поспать", "", "", "Выпить снадобье",
                      "Оставить", "", "Искать старосту", "", "Уйти и пойти куда глаза глядят", "Искать выход", "", "", "Искать таверну", "", "",
                      "", "", "", "", "Ударить старосту", "", "", ""]

# Текста на третью кнопку
third_button_text = ["Осмотреться", "", "", "Порыться в карманах", "", "", "", "", "Вернуться назад в лес", "", "", "", "", "", "", "", "", "",
                     "Искать таверну", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

# Текста для описаний событий
event_text = ["Вы открываете глаза. Вокруг лес. Вы ничего не помните.", "Вокруг все еще лес, в какую сторону не посмотри.",
            """                         Вы усиленно вспоминаете.
Ничего не вспомнили, но от напряжения заболела голова.""", """Пора решать что делать, потому что вы чувствуете голод.
    Да и в целом всю жизнь провести в лесу так себе идея. """, "Эмм... На вашей одежде нет карманов.", """                         Вы усиленно вспоминаете.
Ничего не вспомнили, но от напряжения заболела голова.""", "Вокруг все еще лес, в какую сторону не посмотри.", """На ваш крик откликнулся только дикий енот и сильно покусал вас.
            Задерживаться здесь вам больше не хочется""", "Вы вышли в какое то поле. Где-то вдалеке кучка крестьян копают землю.",
              """Крестьяне приняли вас за того, кто спер их урожай и сильно избили.""", "На удивление было тепло и мягко. Вы хорошо выспались", "Вы наткнулись на старую избу. Выглядит заброшенной",
              "Вы снова заблудились. А что вы ожидали?", "Ничего другого вы не нашли, только устали. Заночевать пришлось в поле.", "К сожалению вы ничего не придумали.",
              """Внутри не очень много всего.
               Вы нашли кровать и странное снадобье на столе.""", "Спустя много времени вы нашли только странный гриб.", """Вы легли лицом на ежа, лежащего под листьями.
               Ёж остался невредим, чего не скажешь о вашем лице.""", "Спустя долгое время вы пришли в какую то деревню.", """Это была плохая идея.
               Хотя бы смерть получилась быстрой.""", """      Утром странное снадобье исчезло.
       Вы начали думать, что упустили какую то невероятную возможность.
       Но дальше надо что то делать.""", "Неожиданно гриб придает вам сил. А еще вы стали понимать зверей", "Ну и ладно. Не очень то и хотелось.",
              "К удивлению, вы не нашли", """Вы застали чью то жену не совсем одетой и заслуженно получили в морду.
              А что, разве не учили стучаться?""", "Вы нашли старосту. Он вглядывается в вас, пытаясь узнать.", "Остается только выпить. Зачем еще идти в таверну?",
              """Вы выбрали остаться в хижине на окраине леса.
               Всю оставшуюся жизнь вы прожили одиноким отщельником""", """ Всю ночь вы разговаривали со зверями. 
               Утром же вы проснулись в поле и снова ничего не помните.
               Ну а что, не надо кушать незнакомые грибы. 
               Зато от зверей в вашем воображении вы узнали путь до деревни.""", "Не нашли, пришлось с печалью остаться в лесу навечно...", """Похоже вы нашли свое призвание.
               Вы остаетесь на правах помощника трактирщика. 
               А потом и сами становитесь трактирщиком.""", "'Ах ты, ты же спер наш урожай!'", "Вам разрешили. Вы стали обычным крестьянином и прожили обычную жизнь.",
              "В это раз вас били до победного...", """             Вы победили старосту в кулачном бою.
              Жители признали вас новым старостой.
              Теперь в вашем распоряжение целая деревня,
               где вы проживете отличную жизнь."""]

# Ветвление сюжета
def first(parametr):
    if parametr['front'] == 0:
        parametr['front'] = 3
    elif parametr['front'] == 1:
        parametr['front'] = 3
        parametr['show_third'] = True
    elif parametr['front'] == 2:
        parametr['front'] = 3
        parametr['show_third'] = True
    elif parametr['front'] == 3:
        parametr['front'] = 8
        parametr['back'] = 1
    elif parametr['front'] == 4:
        parametr['front'] = 8
        parametr['back'] = 1
        parametr['show_third'] = True
    elif parametr['front'] == 5:
        parametr['front'] = 3
        parametr['show_second'] = True
        parametr['show_third'] = True
    elif parametr['front'] == 6:
        parametr['front'] = 3
        parametr['show_second'] = True
        parametr['show_third'] = True
    elif parametr['front'] == 7:
        parametr['front'] = 8
        parametr['back'] = 1
        parametr['show_second'] = True
        parametr['show_third'] = True
    elif parametr['front'] == 8:
        parametr['front'] = 9
        parametr['show_third'] = False
        parametr['life'] -= 1
        parametr['thief'] = True
    elif parametr['front'] == 9:
        parametr['front'] = 10
        parametr['life'] += 1
        parametr['show_second'] = False
    elif parametr['front'] == 10:
        parametr['front'] = 14
    elif parametr['front'] == 11:
        parametr['front'] = 15
        parametr['back'] = 3
    elif parametr['front'] == 12:
        parametr['front'] = 16
    elif parametr['front'] == 13:
        parametr['front'] = 14
    elif parametr['front'] == 14:
        parametr['front'] = 18
        parametr['show_second'] = True
        parametr['show_third'] = True
        parametr['back'] = 4
    elif parametr['front'] == 15:
        parametr['front'] = 20
    elif parametr['front'] == 16:
        parametr['front'] = 21
        if parametr['life'] < 3:
            parametr['life'] += 1
    elif parametr['front'] == 17:
        parametr['front'] = 23
    elif parametr['front'] == 18:
        parametr['front'] = 24
        parametr['life'] -= 1
        parametr['show_third'] = False
    elif parametr['front'] == 20:
        parametr['front'] = 27
        parametr['life'] = 0
    elif parametr['front'] == 21:
        parametr['front'] = 28
        parametr['back'] = 1
        parametr['show_second'] = False
        parametr['life'] = 1
    elif parametr['front'] == 22:
        parametr['front'] = 23
    elif parametr['front'] == 23:
        parametr['front'] = 29
        parametr['life'] = 0
    elif parametr['front'] == 24:
        parametr['front'] = 25
        parametr['show_second'] = False
    elif parametr['front'] == 25:
        if parametr['thief']:
            parametr['front'] = 31
            parametr['show_second'] = True
        else:
            parametr['front'] = 32
            parametr['life'] = 0
    elif parametr['front'] == 26:
        parametr['front'] = 30
        parametr['life'] = 0
    elif parametr['front'] == 28:
        parametr['front'] = 18
        parametr['show_second'] = True
        parametr['show_third'] = True
        parametr['back'] = 4
    elif parametr['front'] == 31:
        parametr['front'] = 33
        parametr['life'] = 0

def second(parametr):
    if parametr['front'] == 0:
        parametr['front'] = 2
        parametr['show_third'] = False
        parametr['life'] -= 1
    elif parametr['front'] == 1:
        parametr['front'] = 5
        parametr['show_second'] = False
        parametr['life'] -= 1
    elif parametr['front'] == 2:
        parametr['front'] = 6
        parametr['show_second'] = False
    elif parametr['front'] == 3:
        parametr['front'] = 7
        parametr['show_second'] = False
        parametr['show_third'] = False
        parametr['life'] -= 1
    elif parametr['front'] == 4:
        parametr['front'] = 7
        parametr['show_second'] = False
        parametr['life'] -= 1
    elif parametr['front'] == 8:
        parametr['front'] = 11
        parametr['show_third'] = False
        parametr['back'] = 2
    elif parametr['front'] == 9:
        parametr['front'] = 13
        parametr['show_second'] = False
    elif parametr['front'] == 11:
        parametr['front'] = 13
        parametr['show_second'] = False
        parametr['back'] = 1
    elif parametr['front'] == 12:
        parametr['front'] = 17
        parametr['show_second'] = False
        parametr['life'] -= 1
    elif parametr['front'] == 15:
        parametr['front'] = 19
        parametr['life'] = 0
    elif parametr['front'] == 16:
        parametr['front'] = 22
        parametr['show_second'] = False
    elif parametr['front'] == 18:
        parametr['front'] = 25
        parametr['show_second'] = False
        parametr['show_third'] = False
    elif parametr['front'] == 20:
        parametr['front'] = 18
        parametr['show_third'] = True
        parametr['back'] = 4
    elif parametr['front'] == 21:
        parametr['front'] = 23
        parametr['show_second'] = False
    elif parametr['front'] == 24:
        parametr['front'] = 26
        parametr['back'] = 5
        parametr['show_second'] = False
    elif parametr['front'] == 31:
        parametr['front'] = 34
        parametr['life'] = 0

def third(parametr):
    if parametr['front'] == 0:
        parametr['front']  = 1
        parametr['show_third'] = False
    elif parametr['front'] == 3:
        parametr['front'] = 4
        parametr['show_third'] = False
    elif parametr['front'] == 8:
        parametr['front'] = 12
        parametr['back'] = 0
        parametr['show_third'] = False
    elif parametr['front'] == 18:
        parametr['front'] = 26
        parametr['show_second'] = False
        parametr['show_third'] = False
        parametr['back'] = 5
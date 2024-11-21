# Файл с сюжетным наполнением

class Downloads:
    '''
    Здесь хранятся все файлы

    Методы:
        __init__
    '''
    def __init__(self):
        '''
        Инициализирует экземпляр класса
        parameters:
        returns:
        '''
        # Массив с фонами
        with open('assets/background_image.txt', 'r') as f:
            self.background_list = f.readlines()

        # Массив с музыкой
        with open('assets/music.txt', 'r') as f:
            self.music_list = f.readlines()

        # Массив с картинками для кнопок
        with open('assets/buttom_image.txt', 'r') as f:
            self.button_list = f.readlines()

        # Текста на первую кнопку
        with open('assets/first_button_text.txt', 'r', encoding='utf-8') as f:
            self.first_button_text = f.readlines()

        # Текста на вторую кнопку
        with open('assets/second_button_text.txt', 'r', encoding='utf-8') as f:
            self.second_button_text = f.readlines()

        # Текста на третью кнопку
        with open('assets/third_button_text.txt', 'r', encoding='utf-8') as f:
            self.third_button_text = f.readlines()

        # Текста для описаний событий
        with open('assets/event_text.txt', 'r', encoding='utf-8') as f:
            self.event_text = f.readlines()

class Story:
    '''
    Управляет сюжетом

    Методы:
        __init__
        first
        second
        third
    '''
    def __init__(self):
        '''
        Инициализирует экземпляр класса
        parameters:
        returns:
        '''
        # [Номер момента, состояние второй кнопки, состояние третьей кнопки, номер фона, увеличение жизней]
        self.story_first = {0: [3, True, True, 0, 0],
                           1: [3, True, True, 0, 0],
                           2: [3, True, True, 0, 0],
                           3: [8, True, True, 1, 0],
                           4: [8, True, True, 1, 0],
                           5: [3, True, True, 0, 0],
                           6: [3, True, True, 0, 0],
                           7: [8, True, True, 1, 0],
                           8: [9, True, False, 1, -1], # thief
                           9: [10, False, False, 1, 1],
                           10: [14, False, False, 1, 0],
                           11: [15, True, False, 3, 0],
                           12: [16, True, False, 0, 0],
                           13: [14, False, False, 1, 0],
                           14: [18, True, True, 4, 0],
                           15: [20, True, False, 3, 0],
                           16: [21, True, False, 0, 0], # life < 3, то + 1
                           17: [23, False, False, 0, 0],
                           18: [24, True, False, 4, -1],
                           20: [27, False, False, 3, -3],
                           21: [28, False, False, 1, 0], # life = 1
                           22: [23, False, False, 0, 0],
                           23: [29, False, False, 0, -3],
                           24: [25, False, False, 4, 0],
                           26: [30, False, False, 5, -3],
                           28: [18, True, True, 4, 0],
                           31: [33, False, False, 4, -3]}

        self.story_second = {0: [2, True, False, 0, -1],
                            1: [5, False, False, 0, -1],
                            2: [6, False, False, 0, 0],
                            3: [7, False, False, 0, -1],
                            4: [7, False, False, 0, -1],
                            8: [11, True, False, 2, 0],
                            9: [13, False, False, 1, 0],
                            11: [13, False, False, 1, 0],
                            12: [17, False, False, 0, -1],
                            15: [19, False, False, 3, -3],
                            16: [22, False, False, 0, 0],
                            18: [25, False, False, 4, 0],
                            20: [18, True, True, 4, 0],
                            21: [23, False, False, 0, 0],
                            24: [26, False, False, 5, 0],
                            31: [34, False, False, 4, -3]}

        self.story_third = {0: [1, True, False, 0, 0],
                           3: [4, True, False, 0, 0],
                           8: [12, True, False, 0, 0],
                           18: [26, False, False, 5, 0]}

    def first(self, parametr):
        '''
        Управляет действиями первой кнопки
        parameters: parametr (dict)
        returns:
        '''
        try:
            if parametr['front'] != 25:
                parametr['show_second'] = self.story_first[parametr['front']][1]
                parametr['show_third'] = self.story_first[parametr['front']][2]
                parametr['back'] = self.story_first[parametr['front']][3]
                parametr['life'] += self.story_first[parametr['front']][4] # Просто я изменяю параметр жизни, не зная его значение, и мне кажется константами было бы не очень удобно
                if parametr['front'] == 16:
                    if parametr['life'] < 3:
                        parametr['life'] += 1
                if parametr['front'] == 21:
                    parametr['life'] = 1
                if parametr['front'] == 8:
                    parametr['thief'] = True
                parametr['front'] = self.story_first[parametr['front']][0]
            else:
                if parametr['thief']:
                    parametr['front'] = 31
                    parametr['show_second'] = True
                else:
                    parametr['front'] = 32
                    parametr['life'] = 0
        except KeyError:
            pass

    def second(self, parametr):
        '''
        Управляет действиями второй кнопки
        parameters: parametr (dict)
        returns:
        '''
        try:
            parametr['show_second'] = self.story_second[parametr['front']][1]
            parametr['show_third'] = self.story_second[parametr['front']][2]
            parametr['back'] = self.story_second[parametr['front']][3]
            parametr['life'] += self.story_second[parametr['front']][4]
            parametr['front'] = self.story_second[parametr['front']][0]
        except KeyError:
            pass

    def third(self, parametr):
        '''
        Управляет действиями третьей кнопки
        parameters: parametr (dict)
        returns:
        '''
        try:
            parametr['show_second'] = self.story_third[parametr['front']][1]
            parametr['show_third'] = self.story_third[parametr['front']][2]
            parametr['back'] = self.story_third[parametr['front']][3]
            parametr['life'] += self.story_third[parametr['front']][4]
            parametr['front'] = self.story_third[parametr['front']][0]
        except KeyError:
            pass
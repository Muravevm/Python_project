import pygame
import sys
from src.button import ImageButton
from src.life import*
from src.background import Background
from src.event import Event
from src.story import*

class Game:
    '''
    Основной класс управления игрой

    Методы:
        prep
        run
    '''

    def prep(self):
        '''
        Подготовка всех нужных элементов к началу игры
        parameters:
        returns:
        '''
        # Инициализация pygame
        pygame.init()

        # Параметры экрана
        self.width, self.height = 1280, 800

        self.window_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Quest')

        # Здесь все файлы
        self.downloads = Downloads()

        # Здесь весь сюжет
        self.story = Story()

        # Создание фона и загрузка всех фонов
        self.background = Background(self.width, self.height, "assets/start.png", self.downloads.music_list[0][:-1])
        self.background.draw(self.screen)
        for x in self.downloads.background_list:
            x = x[:-1]
            self.background.load(x)

        # Создание интерфейса жизней
        self.life_first = Life(50, 60, "assets/Life.png")
        self.life_second = Life(50, 120, "assets/Life.png")
        self.life_third = Life(50, 180, "assets/Life.png")

        # Создание кнопок
        self.start_button = ImageButton(self.width / 2 - (400 / 2), 600, 400, 70, "Начать игру", self.downloads.button_list[0][:-1],
                                   self.downloads.button_list[1][:-1])
        self.first_button = ImageButton(self.width / 2 - (400 / 2), 400, 400, 70, "", self.downloads.button_list[0][:-1],
                                   self.downloads.button_list[1][:-1])
        self.second_button = ImageButton(self.width / 2 - (400 / 2), 500, 400, 70, "", self.downloads.button_list[0][:-1],
                                    self.downloads.button_list[1][:-1])
        self.third_button = ImageButton(self.width / 2 - (400 / 2), 600, 400, 70, "", self.downloads.button_list[0][:-1],
                                   self.downloads.button_list[1][:-1])
        self.end_button = ImageButton(self.width / 2 - (400 / 2), 600, 400, 70, "Выйти", self.downloads.button_list[0][:-1],
                                 self.downloads.button_list[1][:-1])

        # Создание описания ситуации
        self.description = Event(self.width / 2 - (800 / 2), 100, 800, 200, "", "assets/test2.png")

        # Загрузка сценария
        for x in self.downloads.first_button_text:
            x = x[:-1]
            self.first_button.load(x)
        for x in self.downloads.second_button_text:
            x = x[:-1]
            self.second_button.load(x)
        for x in self.downloads.third_button_text:
            x = x[:-1]
            self.third_button.load(x)
        for x in self.downloads.event_text:
            x = x[:-1]
            self.description.load(x)

        # Необходимые переменные
        self.start = False
        self.parametr = {'back': 0, 'front': 0, 'show_first': True, 'show_second': True, 'show_third': True, 'running': True,
                    'life': 3, 'thief': False}

    def run(self):
        '''
        Запуск игры
        parameters:
        returns:
        '''
        self.prep()
        running = True
        posion = pygame.USEREVENT

        # Основной цикл
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    # Выход из игры
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == posion:

                    # Переход от стартового экрана к основным действиям
                    self.start = True;
                    self.background.next(self.screen, self.parametr['back'])

                if self.end_button.handle_event(event):

                    # Конец игры
                    running = False
                    pygame.quit()
                    sys.exit()

                if self.start:

                    # Действия
                    if self.first_button.handle_event(event):
                        self.story.first(self.parametr)
                    if self.second_button.handle_event(event):
                        self.story.second(self.parametr)
                    if self.third_button.handle_event(event):
                        self.story.third(self.parametr)
                else:

                    # Стартовая кнопка
                    self.start_button.handle_event(event)

            if self.start:

                #  Условие проигрыша
                if self.parametr['life'] <= 0:
                    self.parametr['show_first'] = False
                    self.parametr['show_second'] = False
                    self.parametr['show_third'] = False
                    self.first_button.is_hovered = False
                    self.second_button.is_hovered = False
                    self.third_button.is_hovered = False
                    self.description.next(self.screen, self.parametr['front'])
                    self.end_button.check_hover(pygame.mouse.get_pos())
                    self.end_button.draw(self.screen)

                else:

                    # Отрисовка состояния
                    self.description.next(self.screen, self.parametr['front'])
                    self.life_first.draw(self.screen, self.parametr['life'] >= 1)
                    self.life_second.draw(self.screen, self.parametr['life'] >= 2)
                    self.life_third.draw(self.screen, self.parametr['life'] >= 3)
                    self.first_button.next(self.screen, self.parametr['front'], self.parametr['show_first'])
                    self.first_button.check_hover(pygame.mouse.get_pos())
                    self.second_button.next(self.screen, self.parametr['front'], self.parametr['show_second'])
                    self.second_button.check_hover(pygame.mouse.get_pos())
                    self.third_button.next(self.screen, self.parametr['front'], self.parametr['show_third'])
                    self.third_button.check_hover(pygame.mouse.get_pos())

            else:

                # Стартовый экран
                self.start_button.check_hover(pygame.mouse.get_pos())
                self.start_button.draw(self.screen)

            pygame.display.flip()

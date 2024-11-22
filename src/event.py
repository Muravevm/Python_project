import pygame

class Event:
    '''
    Класс Событие

    Методы:
        __init__
        load
        draw
        next
    '''
    def __init__(self, x, y, width, height, text, image_path):
        '''
        Инициализирует экземпляр класса
        parameters: x (int), y (int), width (int), height (int), text (str), image_path (str)
        returns:
        '''
        if (0 < x < 1280 - width):
            self.x = x
        else:
            self.x = 240

        if (0 < y < 800 - height):
            self.y = y
        else:
            self.y = 100

        if (0 < width < 1280 - x):
            self.width = width
        else:
            self.width = 800

        if (0 < height < 800 - y):
            self.height = height
        else:
            self.height = 200

        self.text = text

        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect(topleft=(x, y))
        except FileNotFoundError:
            print('Картинка для загрузки не найдена')

        self.texts = []

    def load(self, text):
        '''
        Загружает все текста необходимые для игры
        parameters: text (str)
        returns:
        '''
        font = pygame.font.Font(None, 30)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.texts.append([text_surface, text_rect])

    def draw(self, screen):
        '''
        Отрисовывает описание события на экране
        parameters: screen (Surface)
        returns:
        '''
        current_image = self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def next(self, screen, number):
        '''
        Отрисовывает следующее нужное нам описание события на экране
        parameters: screen (Surface), number (int)
        returns:
        '''
        current_image = self.image
        screen.blit(current_image, self.rect.topleft)
        try:
            screen.blit(self.texts[number][0], self.texts[number][1])
        except IndexError:
            print('Элемента с индексом number нет в массиве')
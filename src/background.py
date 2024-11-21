import pygame

class Background:
    '''
    Класс, отвечающий за задний фон

    Методы:
        __init__
        load
        draw
        next
    '''
    def __init__(self, width, height, image, music):
        '''
        Инициализирует экземпляр класса
        parameters:  width (int), height(int), image(str), music(str)
        returns:
        '''
        self.width = width
        self.height = height

        try:
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (width, height))
        except FileNotFoundError:
            print('Картинка для загрузки не найдена')

        try:
            self.music = pygame.mixer.music.load(music)
            pygame.mixer.music.play(-1)
        except FileNotFoundError:
            print('Музыка для загрузки не найдена')

        self.images = []

    def load(self, image):
        '''
        Загружает все файлы нужные для заднего фона
        parameters: image (str)
        returns:
        '''
        try:
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (self.width, self.height))
            self.images.append(image)
        except FileNotFoundError:
            print('Картинка для загрузки не найдена')

    def draw(self, screen):
        '''
        Отрисовывает задний фон
        parameters:  screen (Surface)
        returns:
        '''
        background_image = self.image
        screen.blit(background_image, (0, 0))

    def next(self, screen, number):
        '''
        Отрисовывает следующий нужный нам фон из загруженных
        parameters:  screen (Surface), number (int)
        returns:
        '''
        try:
            background_image = self.images[number]
            screen.blit(background_image, (0, 0))
        except IndexError:
            print('Элемента с индексом number нет в массиве')
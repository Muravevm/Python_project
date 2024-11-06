import pygame

class Background:
    '''
    Класс Заднего фона

    __init__: Принимает width, height: размеры экрана
                        image: стартовая картинка
                        music: музыка

    draw: Принимает screen: экран
          Отрисовывает задний фон

    load: Принимает image: новый фон
          Загружает в массив готовый к выводу на экран новый фон

    next: Принимает screen: экран
                    number: указание какой фон следует вывести
          Отображает нужный фон
    '''
    def __init__(self, width, height, image, music):
        self.width = width
        self.height = height

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.music = pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

        self.images = []

    def load(self, image):
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (self.width, self.height))
        self.images.append(image)

    def draw(self, screen):
        background_image = self.image
        screen.blit(background_image, (0, 0))

    def next(self, screen, number):
        background_image = self.images[number]
        screen.blit(background_image, (0, 0))
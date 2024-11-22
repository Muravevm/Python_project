import pygame

class Life:
    '''
    Класс жизней

    Методы:
        __init__
        draw
    '''
    def __init__(self, x, y, image):
        '''
        Инициализирует экзепляр класса
        parameters: x (int), y (int), image (str)
        returns:
        '''
        self.x = x
        self.y = y

        try:
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect(topleft=(x, y))
        except FileNotFoundError:
            print('Картинка для загрузки не найдена')

    def draw(self, screen, show):
        '''
        Отрисовывает жизнь на экране, если она нужна
        parameters: screen (Surface), show (bool)
        returns:
        '''
        if show:
            current_image = self.image
            screen.blit(current_image, self.rect.topleft)
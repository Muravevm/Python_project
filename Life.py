import pygame

class Life:
    '''
    Класс жизней

    __init__: Принимает x, y: координаты, где расположить сердечко
                       image: риунок сердечка

    draw: Принимает screen: экран
                    show: указание следует ли отображать жизнь
          Отображает или нет эту жизнь
    '''
    def __init__(self, x, y, image):
        self.x = x
        self.y = y

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen, show):
        if show:
            current_image = self.image
            screen.blit(current_image, self.rect.topleft)
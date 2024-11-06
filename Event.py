import pygame

class Event:
    '''
    Класс Событие

    __init__: Принимает x, y: координаты левого верхнего угла
                        width, height: размеры экрана
                        text: стартовый текст
                        image_path: картинка

    draw: Принимает screen: экран
          Выводит новое описание игровой ситуации, отрисовывает картинку

    load: Принимает text: новый текст
          Загружает в массив готовый к выводу на экран новый текст

    next: Принимает screen: экран
                    number: указание какой текст следует вывести
          Отображает нужный текст
    '''
    def __init__(self, x, y, width, height, text, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.texts = []

    def load(self, text):
        font = pygame.font.Font(None, 30)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.texts.append([text_surface, text_rect])

    def draw(self, screen):
        current_image = self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def next(self, screen, number):
        current_image = self.image
        screen.blit(current_image, self.rect.topleft)
        screen.blit(self.texts[number][0], self.texts[number][1])
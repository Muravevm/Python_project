import pygame

class ImageButton:
    '''
    Класс кнопок

    Методы:
        __init__
        draw
        load
        next
        check_hover
        handle_event
    '''
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None):
        '''
        Инициализирует экземпляр класса
        parameters:  x (int), y (int), width (int), height (int), text (str), image_path (str), hover_image_path (str)
        returns:
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.texts = []

        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
            self.hover_image = self.image
            self.rect = self.image.get_rect(topleft=(x, y))
        except FileNotFoundError:
            print('Картинка для загрузки не найдена')

        if hover_image_path:
            try:
                self.hover_image = pygame.image.load(hover_image_path)
                self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
            except FileNotFoundError:
                print('Картинка для загрузки не найдена')

        self.is_hovered = False

    def draw(self, screen):
        '''
        Отрисовывает кнопку на экране
        parameters:  screen (Surface | SurfaceType = pygame.display.set_mode(window_size))
        returns:
        '''
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def load(self, text):
        '''
        Загружает текст для кнопок
        parameters: text (str)
        returns:
        '''
        font = pygame.font.Font(None, 30)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.texts.append([text_surface, text_rect])

    def next(self, screen, number, show):
        '''
        Отрисовывает следующую нужную кнопку с текстом
        parameters:  screen (Surface), number (int), show (bool)
        returns:
        '''
        if show:
            current_image = self.hover_image if self.is_hovered else self.image
            screen.blit(current_image, self.rect.topleft)
            try:
                screen.blit(self.texts[number][0], self.texts[number][1])
            except IndexError:
                print('Элемента с индексом number нет в массиве')

    def check_hover(self, mouse_pos):
        '''
        Проверяет наведена ли мышь на кнопку
        parameters: mouse_pos (tuple[int, int])
        returns:
        '''
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        '''
        Выполняет определенные действия при нажатии
        parameters: event (Event)
        returns: bool
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            return True

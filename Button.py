import pygame

class ImageButton:
    '''
    Класс кнопок

    __init__: Принимает x, y: координаты левого верхнего угла
                        width, height: размеры кнопки
                        text: стартовый текст
                        image_path, hover_image_path: рисунок и рисунок при наведении мыши

    draw: Принимает screen: экран
          Отрисовывает кнопку

    load: Принимает text: новый текст кнопки
          Загружает в массив готовый к выводу на экран текст

    next: Принимает screen: экран
                    number: указание какой текст следует вывести
                    show: указание следует ли отображать кнопку
          Если кнопку следует отображать, то отображает с новым текстом, иначе скрывает.

    check_hovered: Принимает mouse_pos: поизиция мыши
                   Проверяет наведена ли мышь на кнопку

    handle_event: Принимает event: событие
                  Выполняет опрделенные действия при нажатии
                  Возвращает True, что ознает то, что нажатие случилось
    '''
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.texts = []

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def load(self, text):
        font = pygame.font.Font(None, 30)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.texts.append([text_surface, text_rect])

    def next(self, screen, number, show):
        if show:
            current_image = self.hover_image if self.is_hovered else self.image
            screen.blit(current_image, self.rect.topleft)

            screen.blit(self.texts[number][0], self.texts[number][1])

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            return True

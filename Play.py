import pygame
import sys
from Button import ImageButton
from Life import*
from Background import Background
from pygame.examples.moveit import WIDTH
from Event import Event
from Story import*

def main():
    '''
    Основная функция запускающая сам цикл игры

    Ничего не возвращает и ничего не принимает
    '''
    # Инициализация pygame
    pygame.init()

    # Параметры экрана
    width, height = 1280, 800

    window_size = (width, height)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Quest')

    # Создание фона и загрузка всех фонов
    background = Background(width, height, "assets/start.png", music_list[0])
    background.draw(screen)
    for x in background_list:
        background.load(x)

    # Создание интерфейса жизней
    life_first = Life(50, 60, "assets/Life.png")
    life_second = Life(50, 120, "assets/Life.png")
    life_third = Life(50, 180, "assets/Life.png")

    # Создание кнопок
    start_button = ImageButton(width / 2 - (400 / 2), 600, 400, 70, "Начать игру", button_list[0], button_list[1])
    first_button = ImageButton(width / 2 - (400 / 2), 400, 400, 70, "", button_list[0], button_list[1])
    second_button = ImageButton(width / 2 - (400 / 2), 500, 400, 70, "", button_list[0], button_list[1])
    third_button = ImageButton(width / 2 - (400 / 2), 600, 400, 70, "", button_list[0], button_list[1])
    end_button = ImageButton(width / 2 - (400 / 2), 600, 400, 70, "Выйти", button_list[0], button_list[1])

    # Создание описания ситуации
    description = Event(width / 2 - (800 / 2), 100, 800, 200, "", "assets/test2.png")

    # Загрузка сценария
    for x in first_button_text:
        first_button.load(x)
    for x in second_button_text:
        second_button.load(x)
    for x in third_button_text:
        third_button.load(x)
    for x in event_text:
        description.load(x)

    # Необходимые переменные
    posion = pygame.USEREVENT
    start = False
    parametr = {'back': 0, 'front': 0, 'show_first': True, 'show_second': True, 'show_third': True, 'running': True, 'life': 3, 'thief': False}
    running = True

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
                start = True;
                background.next(screen, parametr['back'])

            if end_button.handle_event(event):

                # Конец игры
                running = False
                pygame.quit()
                sys.exit()

            if start:

                # Действия
                if first_button.handle_event(event):
                    first(parametr)
                if second_button.handle_event(event):
                    second(parametr)
                if third_button.handle_event(event):
                    third(parametr)
            else:

                # Стартовая кнопка
                start_button.handle_event(event)

        if start:

            #  Условие проигрыша
            if parametr['life'] <= 0:
                parametr['show_first'] = False
                parametr['show_second'] = False
                parametr['show_third'] = False
                end_button.check_hover(pygame.mouse.get_pos())
                end_button.draw(screen)

            # Отрисовка состояния
            description.next(screen, parametr['front'])
            life_first.draw(screen, parametr['life'] // 1)
            life_second.draw(screen, parametr['life'] // 2)
            life_third.draw(screen, parametr['life'] // 3)
            first_button.next(screen, parametr['front'], parametr['show_first'])
            first_button.check_hover(pygame.mouse.get_pos())
            second_button.next(screen, parametr['front'], parametr['show_second'])
            second_button.check_hover(pygame.mouse.get_pos())
            third_button.next(screen, parametr['front'], parametr['show_third'])
            third_button.check_hover(pygame.mouse.get_pos())

        else:

            # Стартовый экран
            start_button.check_hover(pygame.mouse.get_pos())
            start_button.draw(screen)

        pygame.display.flip()

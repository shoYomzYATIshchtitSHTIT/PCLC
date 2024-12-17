import pygame
import pygame_menu

pygame.display.set_caption('Главное меню')
surface = pygame.display.set_mode((1000, 675))
pygame.init()


def start_the_game():
    import main


def about_program():
    pass


menu = pygame_menu.Menu('Fancy Space', 1000, 675, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)
menu.mainloop(surface)

import pygame
from settings import Settings
from pachimari import Pachimari
import game_functions as gf


def run_game():
    pygame.init()
    pa_settings = Settings
    screen = pygame.display.set_mode((pa_settings.screen_width, pa_settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Pachimary Defender')
    pachimari = Pachimari(pa_settings, screen)

    while True:
        gf.check_events(pachimari)
        pachimari.update()
        gf.update_screen(pa_settings, screen, pachimari)

run_game()

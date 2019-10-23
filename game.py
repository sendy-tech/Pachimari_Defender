import pygame
from settings import Settings
from pachimari import Pachimari
from Reaper import Reaper
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    pa_settings = Settings
    screen = pygame.display.set_mode((pa_settings.screen_width, pa_settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Pachimary Defender')
    pachimari = Pachimari(pa_settings, screen)
    bullets = Group()
    reaper = Reaper(pa_settings, screen)

    while True:
        gf.check_events(pa_settings, screen, pachimari, bullets)
        pachimari.update()
        gf.update_bullets(bullets)
        gf.update_screen(pa_settings, screen, pachimari, reaper, bullets)

run_game()

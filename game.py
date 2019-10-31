import pygame
from settings import Settings
from pachimari import Pachimari
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    pygame.init()
    pa_settings = Settings
    screen = pygame.display.set_mode((pa_settings.screen_width, pa_settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Pachimary Defender')
    stats = GameStats(pa_settings)
    pachimari = Pachimari(pa_settings, screen)
    bullets = Group()
    reapers = Group()
    stars = Group()
    gf.create_fleet(pa_settings, screen, pachimari, reapers)
    gf.create_fleet_stars(pa_settings, screen, stars)

    while True:
        gf.check_events(pa_settings, screen, pachimari, bullets)
        if stats.game_active:
            pachimari.update()
            gf.update_bullets(pa_settings, screen, pachimari, reapers, bullets)
            gf.update_reapers(pa_settings, stats, screen, pachimari, reapers, bullets)
        gf.update_screen(pa_settings, screen, pachimari, reapers, bullets, stars)

run_game()

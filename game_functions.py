import sys
import pygame
from bullet import Bullet
from reaper import Reaper
from stars import Star_m
from random import randint


def chech_keydown_events(event, pa_settings, screen, pachimari, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        pachimari.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        pachimari.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(pa_settings, screen, pachimari, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullet(pa_settings, screen, pachimari, bullets):
    if len(bullets) < pa_settings.bullets_allowed:
        new_bullet = Bullet(pa_settings, screen, pachimari)
        bullets.add(new_bullet)


def get_numbers_reapers_x(pa_settings, reaper_width):
    available_space_X = pa_settings.screen_width - 2 * reaper_width
    numbers_reapers_x = int(available_space_X / (2 * reaper_width))
    return numbers_reapers_x


def get_numbers_stars_x(pa_settings, star_width):
    available_space_star_X = pa_settings.screen_width - 6 * star_width
    numbers_stars_x = int(available_space_star_X / (2 * star_width))
    return numbers_stars_x


def get_number_rows(pa_settings, pachimari_height, reaper_height):
    available_space_y = (pa_settings.screen_height - (3 * reaper_height) - pachimari_height)
    numbers_row = int(available_space_y / (2 * reaper_height))
    return numbers_row


def get_number_stars_rows(pa_settings, star_height):
    numbers_star_row = int(pa_settings.screen_height / (2 * star_height))
    return numbers_star_row


def create_reaper(pa_settings, screen, reapers, reaper_number, row_number):
    reaper = Reaper(pa_settings, screen)
    reaper_width = reaper.rect.width
    reaper.x = reaper_width + 2 * reaper_width * reaper_number
    reaper.rect.x = reaper.x
    reaper.rect.y = reaper.rect.height + 2 * reaper.rect.height * row_number
    reapers.add(reaper)


def create_star(pa_settings, screen, stars, star_number, star_row_number):
    star = Star_m(pa_settings, screen)
    star_width = star.rect.width
    random_number = randint(-50, 50)
    star.x = star_width + 6 * star_width * star_number + random_number
    star.rect.x = star.x - 10
    star.rect.y = star.rect.height + 6 * star.rect.height * star_row_number + random_number
    stars.add(star)


def create_fleet(pa_settings, screen, pachimari, reapers):
    reaper = Reaper(pa_settings, screen)
    number_reapers_x = get_numbers_reapers_x(pa_settings, reaper.rect.width)
    number_rows = get_number_rows(pa_settings, pachimari.rect.height, reaper.rect.height)
    for row_number in range(number_rows):
        for reaper_number in range(number_reapers_x):
            create_reaper(pa_settings, screen, reapers, reaper_number, row_number)


def create_fleet_stars(pa_settings, screen, stars):
    star = Star_m(pa_settings, screen)
    numbers_stars_x = get_numbers_stars_x(pa_settings, star.rect.width)
    star_number_rows = get_number_stars_rows(pa_settings, star.rect.height)
    for star_row_number in range(star_number_rows):
        for star_number in range(numbers_stars_x):
            create_star(pa_settings, screen, stars, star_number, star_row_number)


def chech_keyup_events(event, pachimari):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        pachimari.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        pachimari.moving_left = False


def check_events(pa_settings, screen, pachimari, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chech_keydown_events(event, pa_settings, screen, pachimari, bullets)
        elif event.type == pygame.KEYUP:
            chech_keyup_events(event, pachimari)


def update_screen(pa_settings, screen, pachimari, reapers, bullets, stars):
    screen.fill(pa_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    stars.draw(screen)
    pachimari.blitme()
    reapers.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

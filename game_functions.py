import sys
import pygame
from bullet import Bullet
from reaper import Reaper


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


def get_number_rows(pa_settings, pachimari_height, reaper_height):
    available_space_y = (pa_settings.screen_height - (3 * reaper_height) - pachimari_height)
    numbers_row = int(available_space_y / (2 * reaper_height))
    return numbers_row


def create_reaper(pa_settings, screen, reapers, reaper_number, row_number):
    reaper = Reaper(pa_settings, screen)
    reaper_width = reaper.rect.width
    reaper.x = reaper_width + 2 * reaper_width * reaper_number
    reaper.rect.x = reaper.x
    reaper.rect.y = reaper.rect.height + 2 * reaper.rect.height * row_number
    reapers.add(reaper)


def create_fleet(pa_settings, screen, pachimari,  reapers):
    reaper = Reaper(pa_settings, screen)
    number_reapers_x = get_numbers_reapers_x(pa_settings, reaper.rect.width)
    number_rows = get_number_rows(pa_settings, pachimari.rect.height, reaper.rect.height)
    for row_number in range(number_rows):
        for reaper_number in range(number_reapers_x):
            create_reaper(pa_settings, screen, reapers, reaper_number, row_number)



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


def update_screen(pa_settings, screen, pachimari, reapers,  bullets):
    screen.fill(pa_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pachimari.blitme()
    reapers.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

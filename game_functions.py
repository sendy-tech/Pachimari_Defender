import sys
import pygame
from bullet import Bullet


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


def update_screen(pa_settings, screen, pachimari, reaper,  bullets):
    screen.fill(pa_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pachimari.blitme()
    reaper.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

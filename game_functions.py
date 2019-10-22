import sys
import pygame


def chech_keydown_events(event, pachimari):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        pachimari.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        pachimari.moving_left = True


def chech_keyup_events(event, pachimari):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        pachimari.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        pachimari.moving_left = False


def check_events(pachimari):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chech_keydown_events(event, pachimari)
        elif event.type == pygame.KEYUP:
            chech_keyup_events(event, pachimari)


def update_screen(pa_settings, screen, pachimari):
    screen.fill(pa_settings.bg_color)
    pachimari.blitme()
    pygame.display.flip()

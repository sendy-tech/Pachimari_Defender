import sys
import pygame


def check_events(pachimari):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pachimari.moving_right = True
            elif event.key == pygame.K_LEFT:
                pachimari.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pachimari.moving_right = False
            elif event.key == pygame.K_LEFT:
                pachimari.moving_left = False

def update_screen(pa_settings, screen, pachimari):
    screen.fill(pa_settings.bg_color)
    pachimari.blitme()
    pygame.display.flip()

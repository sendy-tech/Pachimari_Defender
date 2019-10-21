import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, pa_settings, screen, pachimari):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, pa_settings.bullet_width, pa_settings.bullet_height)
        self.rect.centerx = pachimari.rect.centerx
        self.rect.top = pachimari.rect.top
        self.y = float(self.rect.y)
        self.color = pa_settings.bullet_color
        self.speed_factor = pa_settings.bullet_speed_factor


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

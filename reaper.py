import pygame
from pygame.sprite import Sprite


class Reaper(Sprite):
    def __init__(self, pa_settings, screen):
        super(Reaper, self).__init__()
        self.screen = screen
        self.pa_settings = pa_settings
        self.image = pygame.image.load('images/reaper.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)
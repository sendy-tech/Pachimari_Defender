import pygame
from pygame.sprite import Sprite


class Star_l(Sprite):
    def __init__(self, pa_settings, screen):
        super(Star_l, self).__init__()
        self.screen = screen
        self.pa_settings = pa_settings
        self.image = pygame.image.load('images/star_l.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Star_m(Sprite):
    def __init__(self, pa_settings, screen):
        super(Star_m, self).__init__()
        self.screen = screen
        self.pa_settings = pa_settings
        self.image = pygame.image.load('images/star_m.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Star_s(Sprite):
    def __init__(self, pa_settings, screen):
        super(Star_s, self).__init__()
        self.screen = screen
        self.pa_settings = pa_settings
        self.image = pygame.image.load('images/star_s.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

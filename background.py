__author__ = 'luta'

import pygame

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def drawOnDisplay(self, display):
        display.blit(self.image, self.rect)

    def scale(self, dimension):
        self.image = pygame.transform.scale(self.image, dimension)
        self.rect = self.image.get_rect()
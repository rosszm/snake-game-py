# Snake V 1.0

# food.py()
# python file containing the Food class

# Created By: Zack Ross
# Last Updated: May 6, 2017


import pygame
from pygame.locals import *
import random as r


class Food(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initializes the Food object.

        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,15])
        self.image.fill((250, 50, 50), pygame.Rect(1, 1, 13, 13))
        self.rect = self.image.get_rect()

        self.rect.x = r.randrange(15, 615, 15)
        self.rect.y = r.randrange(75, 675, 15)

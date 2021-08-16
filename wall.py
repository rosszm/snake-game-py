# Snake V 1.0

# wall.py()
# python file containing the Wall class

# Created By: Zack Ross
# Last Updated: May 6, 2017


import pygame
from pygame.locals import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, rect):
        """
        Initializes the Wall object.

        :param pos: the x and y coordinates of the wall; tuple
        :param rect: the width and height of the rectangle; tuple
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([rect[0], rect[1]])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

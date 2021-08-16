# Snake V 1.0

# snake.py()
# python file containing the Snake class

# Created By: Zack Ross
# Last Updated: May 6, 2017


import pygame
from pygame.locals import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        Initializes the Snake object.

        :param x: starting position for x; integer
        :param y: starting position for y; integer
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.image.fill((250, 250, 250), pygame.Rect(1, 1, 13, 13))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_x = 0
        self.speed_y = 0

        self.tail = []
        self.history = [[0, 0]]
        self.length = 1

    def direction(self, x, y):
        """
        Sets the direction and speed that the Snake object will travel.

        :param x: the x speed (left; negative, no direction; 0, right; positive); integer
        :param y: the y direction (up; negative, no direction; 0, down; positive); integer
        :return: None
        """
        if self.length == 1:
            self.speed_x = x
            self.speed_y = y
        else:
            if not(x < 0 < self.speed_x or x > 0 > self.speed_x):
                self.speed_x = x
            if not(y < 0 < self.speed_y or y > 0 > self.speed_y):
                self.speed_y = y

    def update(self):
        """
        Updates the position of the Snake object.

        :return: None
        """
        nxt = [self.rect.x, self.rect.y]

        for idx in range(self.length - 1):
            past = self.history[idx + 1]
            self.history[idx + 1] = nxt
            nxt = past

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.history[0] = [self.rect.x, self.rect.y]

        if self.length > 1:
            self.tail[0] = self.history[0]

        for idx in range(self.length - 1):
            self.tail[idx] = self.history[idx + 1]

    def show(self, screen):
        """
        Displays the Snake object on the screen

        :param: screen
        :return: None
        """
        screen.blit(self.image, self.rect)

        tail_block = pygame.Surface([15, 15])
        tail_block.fill((250, 250, 250), pygame.Rect(1, 1, 13, 13))

        for block_pos in self.tail:
            screen.blit(tail_block, block_pos)

    def grow(self):
        """
        Adds tail blocks to the Snake object.

        :return: None
        """
        new_block_pos = self.history[-1]

        tail_length = 5

        for i in range(tail_length):
            self.tail.append([new_block_pos])
            self.history.append(new_block_pos)

        self.length += tail_length

    def reset(self, x, y):
        """
        Resets all the Snake object's values to their original starting values.

        :param x: x-coordinate in pixels; integer
        :param y: y-coordinate in pixels; integer
        :return:
        """
        self.rect.x = x
        self.rect.y = y

        self.speed_x = 0
        self.speed_y = 0

        self.tail = []
        self.history = [[0, 0]]
        self.length = 1

    def collide_self(self):
        """
        Checks if the Snake object has run into its tail.

        :return: True, if the head touches the tail; False otherwise
        """
        return [self.rect.x, self.rect.y] in self.tail

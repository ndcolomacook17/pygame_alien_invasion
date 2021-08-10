# Creating the Ship class

import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its start position"""
        self.screen = screen

        # Load ship image and get its rect, image.load() returns surface
        # representing the ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at bottom center of screen
        #x coord
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at its current loication"""
        self.screen.blit(self.image, self.rect)

import pygame
import random
from constants import *
from shape import CircleShape
from player import Player

class DeathAnimation(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("imgs/bom.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect(center=position)
        
        self.start_time = pygame.time.get_ticks()
        self.duration = 500  # Duration in milliseconds

    def update(self, dt=None):  # Add dt as an optional parameter
        if pygame.time.get_ticks() - self.start_time > self.duration:
            self.kill()  # Remove the death animation after duration

    def draw(self, screen):
        """Draw the DeathAnimation on the given screen."""
        screen.blit(self.image, self.rect.topleft)

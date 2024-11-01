import pygame
from constants import *
from shape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
        self.image = pygame.image.load("imgs/bullet2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y)) 
        


    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
        screen.blit(rotated_image, rotated_rect)
        
    def update(self, dt):
        self.position += self.velocity * dt
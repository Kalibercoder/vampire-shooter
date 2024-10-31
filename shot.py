import pygame
from constants import *
from shape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.image = pygame.image.load("imgs/bullets.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))  # Initialize rect for positioning
        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
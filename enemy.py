import pygame
import random
from constants import *
from shape import CircleShape
from player import *


class Enemy(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.image.load("imgs/dog2.png").convert_alpha()  
        self.image = pygame.transform.scale(self.image, (100, 100))  
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))  
        self.speed = ENEMY_SPEED

    def chase(self, Player):
        direction = Player - self.position
        if direction.length() > 0:  
            direction = direction.normalize()  
        self.velocity = direction * self.speed


    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)  

    def update(self, dt):
        self.position += self.velocity * dt  
        self.rect.center = self.position.xy

    def split(self):
        self.kill() 

        if self.radius <= ENEMY_MIN_RADIUS:
            return  

        
        random_angle = random.uniform(20, 50)

        
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ENEMY_MIN_RADIUS
        enemy_a = Enemy(self.position.x, self.position.y, new_radius)
        enemy_a.velocity = a * 1.2  # Adjust speed
        enemy_b = Enemy(self.position.x, self.position.y, new_radius)
        enemy_b.velocity = b * 1.2  # Adjust speed

        return enemy_a, enemy_b
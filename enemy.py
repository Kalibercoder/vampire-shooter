import pygame
import random
from constants import *
from shape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.image.load("imgs/alien.png").convert_alpha()  # Load the asteroid image
        self.image = pygame.transform.scale(self.image, (100, 100))  # Scale the image to your desired size
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))  # Set the rect to help with positioning

    def draw(self, screen):
        # Draw the asteroid image instead of a white circle
        screen.blit(self.image, self.rect.topleft)  # Draw the image at the current position

    def update(self, dt):
        self.position += self.velocity * dt  # Update the position based on velocity
        self.rect.center = (self.position.x, self.position.y)  # Update rect position to match the current position

    def split(self):
        self.kill()  # Remove this asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # If the asteroid is too small, don't split further

        # Randomize the angle of the split
        random_angle = random.uniform(20, 50)

        # Create two new asteroids with updated velocity and radius
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = a * 1.2  # Adjust speed
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = b * 1.2  # Adjust speed

        return asteroid_a, asteroid_b
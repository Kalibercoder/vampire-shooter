from shape import CircleShape
from constants import *
import pygame  
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):  
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        # Load the image and store an original copy for rotation
        self.image = pygame.image.load("imgs/shooter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.original_image = self.image
        # Get the image rect to help with positioning
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
        screen.blit(rotated_image, rotated_rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:  # Rotate right
            self.rotation += PLAYER_TURN_SPEED * dt

        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            self.rotation += 180  
            self.move(dt)
            self.rotation -= 180  
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        # Shooting logic with a cooldown timer
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_CD
        shot = Shot(self.position.x, self.position.y, self.rotation)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

import pygame
import sys
from constants import *
from shape import CircleShape
from player import *
from shot import Shot
from enemy import *
from enemyfield import *
from score import draw_score
   

def main():
    pygame.init()
    print("Starting Game :)")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    font = pygame.font.Font(None, 36)

    Enemy.containers = (enemys, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    EnemyField.containers = updatable
    enemy_field = EnemyField()

    Player.containers = (updatable, drawable)

    background_image = pygame.image.load("imgs/background.png").convert()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.score = 0  # Initialize player score

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for obj in updatable:
            obj.update(dt)

        for enemy in enemys:
            if enemy.collides_with(player):
                print("Game over!")
                pygame.quit()
                sys.exit()

            for shot in shots:
                if enemy.collides_with(shot):
                    shot.kill()
                    player.score += 10  # Increment score
                    enemy.split()

        screen.blit(background_image, (0, 0))  # Draw background

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Draw the score
        draw_score(screen, player, font)

        pygame.display.flip()  

        # Limit the framerate to 160 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

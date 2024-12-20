import pygame
import sys
from constants import *
from shape import CircleShape
from player import *
from shot import Shot
from enemy import *
from enemyfield import *
from score import draw_score
from deathanimation import DeathAnimation



def main():
    pygame.init()
    print("Starting Game :)")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    enemys = pygame.sprite.Group()

    #This is what I call best pratice :)
    FONT = pygame.font.Font("fonts/font.ttf", 36)
    font = FONT

    # Initialize containers for each class
    Enemy.containers = (enemys, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    EnemyField.containers = updatable
    enemy_field = EnemyField()
    Player.containers = (updatable, drawable)

    background_image = pygame.image.load("imgs/background3.png").convert()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Set up player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.score = 0  

    game_state = PLAYING 

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif game_state == GAME_OVER and event.type == pygame.KEYDOWN:
                
                main()  # Restart the game by calling main() again

        if game_state == PLAYING:
            for obj in updatable:
                obj.update(dt)

            for enemy in enemys:
                enemy.chase(player.position)  # Make the enemy chase the player
                enemy.update(dt)
                if enemy.collides_with(player):
                    print("Game over!")
                    game_state = GAME_OVER  
                    break

                for shot in shots:
                    if enemy.collides_with(shot):
                        shot.kill()
                        death_animation = DeathAnimation(enemy.rect.center)
                        death_animation.add(updatable, drawable)
                        player.score += 10 
                        enemy.split()

            screen.blit(background_image, (0, 0))  

            # Draw all drawable objects
            for obj in drawable:
                obj.draw(screen)
                

            # Draw the score
            draw_score(screen, player, font)

        elif game_state == GAME_OVER:
            screen.blit(background_image, (0, 0))  
            for obj in drawable:
                obj.draw(screen)

            
            game_over_lines = [
            "Game Over!",
            "Press any key to restart",
            f'Score: {player.score}'
            ]
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))  
            screen.blit(overlay, (0, 0))  
            for i, line in enumerate(game_over_lines):
                game_over_text = font.render(line, True, (255, 0, 0))
                text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + i * 40))  # Adjust the spacing
                screen.blit(game_over_text, text_rect)

        pygame.display.flip() 

        # Limit the framerate to 160 FPS
        dt = clock.tick(160) / 1000


if __name__ == "__main__":
    main()
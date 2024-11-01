import pygame 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def draw_score(screen, player, font):
    """Function to render the player's score with a styled background box and icon."""
    
    # Render the score text
    score_text = font.render(f'Score: {player.score}', True, (255, 0, 0))  
    text_width, text_height = score_text.get_size()
    
    # Box dimensions and position
    box_width = text_width + 40   
    box_height = text_height + 20  
    x_position = (SCREEN_WIDTH - box_width) // 2
    y_position = SCREEN_HEIGHT - box_height - 20  

    # Draw the background box (solid black)
    box_color = (0, 0, 0)  
    pygame.draw.rect(screen, box_color, (x_position, y_position, box_width, box_height), border_radius=10)
    
    # Add a border to the box
    border_color = (255, 0, 0)  
    pygame.draw.rect(screen, border_color, (x_position, y_position, box_width, box_height), width=2, border_radius=10)

    # Position the score text inside the box with padding
    text_x = x_position + 20  
    text_y = y_position + (box_height - text_height) // 2  
    
    
    screen.blit(score_text, (text_x, text_y))
# Creating Pygram Window and Responding to user input

# sys imported for CLI functionality (to exit game when user quits)
import sys
import pygame
from settings import Settings
from ship import Ship

#Imports all fxns from this module
import game_functions as gf

def run_game():
    # Init game, make instance of Settings to have display_screen objects,
    # and set background color
    pygame.init()
    ai_settings = Settings()
    display_screen = pygame.display.set_mode((ai_settings.screen_width,
    ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")
    #bg_color = (230, 230, 230)

    # Make a ship instance
    ship = Ship(display_screen)



    # Start the main loop for the game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, display_screen, ship)


# Maybe use if __name__ == '__main__': here
run_game()

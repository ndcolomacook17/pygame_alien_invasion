# script used to refactor and clean up code
# Don't need to import sys directly into main program file, only being used in
#this module
import sys
import pygame

# Takes care of event loop
def check_events():
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event in pygame.event.get() == pygame.QUIT:
            sys.exit()

# Takes care of updating the screen
def update_screen(ai_settings, screen, ship):
    """Update images on screen and flip to new screen"""
    # Redraw screen during each pass thru loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Makes most recently drawn screen visible
    pygame.display.flip()

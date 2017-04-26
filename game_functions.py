import sys
import pygame

def check_events(hero):
    """Checks to see if a key is pressed."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hero)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)

def check_keydown_events(event, hero):
    """Responds to key presses."""
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
    elif event.key == pygame.K_UP:
        hero.moving_up = True
    elif event.key == pygame.K_DOWN:
        hero.moving_down =  True

def check_keyup_events(event, hero):
    """Responds to key releases."""
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False
    elif event.key == pygame.K_UP:
        hero.moving_up = False
    elif event.key == pygame.K_DOWN:
        hero.moving_down =  False


def update_screen(ai_settings, screen, hero):
    """Update the screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    hero.blitme()

    # Display the most recently rendered screen
    pygame.display.flip()

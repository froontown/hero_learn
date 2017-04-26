import sys
import pygame
from settings import Settings
from hero import Hero
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("BULLETS AND MOVEMENT XTREME")

    # Make the hero!
    hero = Hero(ai_settings, screen)

    # The game loop
    while True:

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        gf.check_events(hero)
        hero.update()
        gf.update_screen(ai_settings, screen, hero)

run_game()

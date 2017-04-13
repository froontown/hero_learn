import sys
import pygame
from settings import Settings
from hero import Hero
import game_functions as gf

def run():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("BULLETS AND MOVEMENT XTREME")

    # Make the hero!
    hero = Hero(ai_settings, screen)

    # The game loop
    while True:

        gf.check_events(hero)
        hero.update()
        gf.update_screen(ai_settings, screen, hero)

run()

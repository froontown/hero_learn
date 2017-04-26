import pygame

class Hero():
    """A class for the main character."""

    def __init__(self, ai_settings, screen):
        """Initialize the Hero!"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('assets/images/knight.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # For the decimals in hero's speed:
        # self.rect.centerx = float(self.rect.centerx)
        # self.rect.centery = float(self.rect.centery)

    def update(self):
        """Going to check the movement of the hero."""
        if self.moving_left > 0:
            self.rect.centerx -= self.ai_settings.hero_speed_factor

        if self.moving_right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.hero_speed_factor

        if self.moving_up and self.rect.top < self.screen_rect.top:
            self.rect.centery -= self.ai_settings.hero_speed_factor

        if self.moving_down and self.rect.width < 0:
            self.rect.centery += self.ai_settings.hero_speed.factor

        # if self.moving_left:
        #     self.rect.centerx -= self.ai_settings.hero_speed_factor
        #
        # if self.moving_right:
        #     self.rect.centerx += self.ai_settings.hero_speed_factor
        #
        # if self.moving_up:
        #     self.rect.centery -= self.ai_settings.hero_speed_factor
        #
        # if self.moving_down:
        #     self.rect.centery += self.ai_settings.hero_speed_factor

        # Update rect object from self.center
        # self.rect.centerx = self.centerx
        # self.rect.centery = self.centery

    def blitme(self):
        """Draws the hero!"""
        self.screen.blit(self.image, self.rect)

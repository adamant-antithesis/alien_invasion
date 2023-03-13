import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class for ship control."""

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the image of the ship and get a rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving the real coordinate of the center of the ship.
        self.x = float(self.rect.x)

        # Movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the "Movement"."""
        # Updates attribute x.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Updating the rect attribute based on self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
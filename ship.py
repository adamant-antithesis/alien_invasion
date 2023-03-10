import pygame


class Ship:
    """Class for ship control."""

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image of the ship and get a rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents one alien."""

    def __init__(self, ai_game):
        """Initializes the alien and sets its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settigs = ai_game.settings

        # Load the alien image and assign the rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()

        # Each new alien appears in the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save the exact horizontal position of the alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moves the alien to the right."""
        self.x += (self.settigs.alien_speed * self.settigs.fleet_direction)
        self.rect.x = self.x

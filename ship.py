import pygame


class Ship:
    """Class for ship control."""

    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image of the ship and get a rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the "Movement"."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)

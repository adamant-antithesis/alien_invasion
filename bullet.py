import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class for controlling projectiles fired by a ship."""

    def __init__(self, ai_game):
        """Spawns a projectile object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a projectile at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The position of the projectile is stored in real format.
        self.y = float(self.rect.y)

    def update(self):
        """Moves the projectile up the screen."""
        # Update the position of the projectile in real format.
        self.y -= self.settings.bullet_speed
        # Update the position of the rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying a projectile on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

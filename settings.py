class Settings:
    """A class for storing all Alien Invasion game settings."""

    def __init__(self):
        """Initializes game settings."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (19, 69, 138)

        # Ship parameters
        self.ship_speed = 1.5

        # Bullets parameters
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

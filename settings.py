class Settings:
    """A class for storing all Alien Invasion game settings."""

    def __init__(self):
        """Initializes game settings."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (19, 69, 138)

        # Ship parameters
        self.ship_speed = 0.9

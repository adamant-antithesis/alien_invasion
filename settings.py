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
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien parameters
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 indicates movement to the right; and -1 - to the left.
        self.fleet_direction = 1

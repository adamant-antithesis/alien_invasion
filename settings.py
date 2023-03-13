class Settings:
    """A class for storing all Alien Invasion game settings."""

    def __init__(self):
        """Initializes static game settings."""
        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (19, 69, 138)

        # Ship parameters
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullets parameters
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien parameters
        self.alien_speed = 1.3
        self.fleet_drop_speed = 10
        # fleet_direction = 1 indicates movement to the right; and -1 - to the left.
        self.fleet_direction = 1

        # Speed up the game
        self.speedup_scale = 1.1
        # The rate of increase in the cost of aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change during the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 means moving to the right; and -1 - to the left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increases alien speed and cost settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


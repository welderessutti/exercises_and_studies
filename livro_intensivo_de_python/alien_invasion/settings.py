class Settings:
    """A class to store all Alien Invasion settings."""

    def __init__(self):
        """Starts the game settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Spaceship settings.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # Bullets settings.
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Aliens settings.
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 1
        # Fleet_direction equal to 1 represents the right; -1 represents the left.
        self.fleet_direction = 1

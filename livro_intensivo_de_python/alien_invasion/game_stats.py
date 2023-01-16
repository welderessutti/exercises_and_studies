class GameStats:
    """Stores Alien Invasion stats."""
    def __init__(self, ai_settings):
        """Starts statistical data."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Starts the Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Starts statistical data that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit

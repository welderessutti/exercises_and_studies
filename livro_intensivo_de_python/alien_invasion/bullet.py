import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class manages the bullets fired by the spaceship."""

    def __init__(self, ai_settings, screen, ship):
        """Creates an object to the bullet at the spaceship's current position."""
        super().__init__()
        self.screen = screen
        # Creates a rect to the bullet in (0, 0) and then defines the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Stores the bullet position like a decimal value.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up on the screen."""
        # Updates the bullet decimal position.
        self.y -= self.speed_factor
        # Updates the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

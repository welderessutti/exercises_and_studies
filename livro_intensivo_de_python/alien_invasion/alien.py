import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A Class representing a single Alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initializes the Alien and sets its inicial position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Loads the Alien image and sets its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        # Starts each new Alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Stores the exactly Alien's position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the Alien in its current position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moves the Alien to the right or to the left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if the Alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

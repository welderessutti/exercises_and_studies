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

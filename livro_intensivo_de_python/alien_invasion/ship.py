import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Starts the spaceship and defines its start position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Loads the spaceship image and gets its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Starts a new spaceship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Stores a decimal value to the center of the spaceship.
        self.center = float(self.rect.centerx)
        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the spaceship position according to the movement flag."""
        # Updates the spaceship center value, and not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Updates the rect object according to the self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the spaceship at its current position."""
        self.screen.blit(self.image, self.rect)

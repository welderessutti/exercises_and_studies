import pygame.font


class Button:

    def __init__(self, ai_settings, screen, msg):
        """Starts the button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Defines the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Builds the rect object of the button and centralizes it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message must be prepared only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Transforms msg in rendered the image and centralizes the text in the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draws a blank button and, then, draws the message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Starts the game and creates an object on the screen.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creates a spaceship.
    ship = Ship(ai_settings, screen)
    # Creates a group that will store the bullets.
    bullets = Group()
    # Creates an Alien.
    alien = Alien(ai_settings, screen)
    # Starts the main loop of the game.
    while True:
        # Observes keybord and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # Redraws the screen on each pass through the loop and makes the most recent screen visible.
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()

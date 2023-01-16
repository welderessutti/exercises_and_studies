import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # Starts the game and creates an object on the screen.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creates an instance to store game statistics data game.
    stats = GameStats(ai_settings)
    # Creates a spaceship, a bullets group, and an Aliens group.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Creates the fleet of Aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Starts the main loop of the game.
    while True:
        # Observes keybord and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # Redraws the screen on each pass through the loop and makes the most recent screen visible.
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

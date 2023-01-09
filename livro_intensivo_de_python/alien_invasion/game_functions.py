import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to keyboard presses."""
    if event.key == pygame.K_RIGHT:
        # Moves the spaceship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Moves the spaceship to the left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responds to keyboard releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responds to keyboard and mouse press events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Updates the images on the screen and switches to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Redraws all the bullets behind the spaceship and the aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    """Updates the position of the bullets and gets free of the old bullets."""
    # Updates the bullets position.
    bullets.update()
    # Gets free of the bullets that disappear.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if the limit has not been reached."""
    # Creates a new bullet and add it to the bullet group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

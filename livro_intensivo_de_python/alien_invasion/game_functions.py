import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Updates the images on the screen and switches to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Redraws all the bullets behind the spaceship and the aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Draws the Play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    # Makes the most recent screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Updates the position of the bullets and gets free of the old bullets."""
    # Updates the bullets position.
    bullets.update()
    # Gets free of the bullets that disappear.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """Responds to the collision between the bullets and Aliens."""
    # Removes any bullet and Alien that collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)
    if len(aliens) == 0:
        # Destroys existing bullets and creates a new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if the limit has not been reached."""
    # Creates a new bullet and add it to the bullet group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creates a full fleet of Aliens."""
    # Creates an Alien and calculates the amount of Aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Creates the fleet of Aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Sets the amount of Aliens that can fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Creates an Alien and position it in row.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Sets the amount of rows with Aliens that can fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Checks if the fleet is on one of the edges and then updates the positions of all Aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Checks if there was a collision between Aliens and the Spaceship.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # Ckecks if there is some Alien that hit the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """Responds appropriately if some Alien reach the edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Makes entire fleet descend and change its direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responds to the fact that the spaceship was hit by an Alien."""
    if stats.ships_left > 0:
        # Decrises ships_left
        stats.ships_left -= 1
        # Empties list of Alien and bullets.
        aliens.empty()
        bullets.empty()
        # Creates a new fleet and centers the spaceship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Takes a break.
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    # Checks if any Aliens reached the bottom of the screen.
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treats this case in the same way as when the spaceship is hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

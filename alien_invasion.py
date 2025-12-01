'''
Lab14 - Alien Invasion pygame. Alisa Dzhoha.
This program is a Pygame game using the Custom Asset Option. I changed the background, ship, aliens, bullets, sounds, and font. I also changed the HUD layout so the score and information show in different places on the screen.
The player moves the ship and shoots aliens to clear the screen. 11/30/2025
'''

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
#from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD


class AlienInvasion:
    """
    This is a main game class. It includes game's loops, events, refresh of the screen, update of the ship.
    """
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
    
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.8)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.8)
        

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False


    def run_game(self):
        """
        This is a loop for the game. It is running while the window for game is still open.
        """
        #Game loop
        while self.running:
            self._check_events()
            if self.game_active:
              self.ship.update()
              self.alien_fleet.update_fleet()
              self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """
        Checks if the ship hits aliens or if aliens reach screen's bottom
        """
        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
  
        #check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        #check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(300)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()


    def _check_game_status(self):
        """
        Checks if the player still has lives or if the game is over
        """
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False    


    def _reset_level(self):
        """
        Clears aliens and bullets, and starts a new level
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        """
        Resets the game and starts again from the beginning
        """
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """
        This method draws background, bullets, ship(cat), and displays everything on the screen."""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

  
    def _check_events(self):
        """
        This method checks for the keyboard presses, it also checks if user decided to quit the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """
        Checks if the play button was clicked by player
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
                
    def _check_keyup_events(self, event):
        """
        Stops the ship when the player stops pressing a key
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
  
    def _check_keydown_events(self, event):
        """
        Method is responsible for ship to move on the screen - left and right. As well as firing lasers (starts).
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


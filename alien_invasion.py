'''
Lab12 - Alien Invasion pygame. Alisa Dzhoha.
This program is a pygame which is built to fire lasers into aliens. This program is based on the tutorial provided by Gabriel Walters. As a part of the lab, the option number two was choosen - customized assets. Game now has a cat as a ship, star as a laser, and a beach-night background. 11/16/2025
'''

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

'''
This is a main game class. It includes game's loops, events, refresh of the screen, update of the ship.
'''
class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
    
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.8)

        self.ship = Ship(self, Arsenal(self))
        self.alien = Alien(self, 10, 10)

    '''
    Thi is a loop for the game. It is running while the window for game is still open.
    '''
    def run_game(self):
        #Game loop
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)
    '''
    This method draws background, bullets, ship (cat), and displays everything on the screen.
    '''
    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien.draw_alien()
        pygame.display.flip()

    '''
    This method checks for the kyboard presses, it also checks if user decided to quit the game.
    '''
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    '''
    Method is responsible for ship to move on the screen - left and right. As well as firing lasers (stars).
    '''
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


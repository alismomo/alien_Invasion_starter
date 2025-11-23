'''
Bullet file creates bullet object that the ship shoots.
'''
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from alien_invasion import AlienInvasion

'''
Class makes a single bullet. loads picture, has a starting position at the ship.
'''
class Alien(Sprite):
  def __init__(self, game: 'AlienInvasion', x:float, y:float):
    super().__init__()
    self.screen = game.screen
    self.boundaries = game.screen.get_rect()
    self.settings = game.settings

    self.image = pygame.image.load(self.settings.alien_file)
    self.image = pygame.transform.scale(self.image, 
          (self.settings.alien_w, self.settings.alien_h)
          )
    
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

    #self.y = float(self.rect.y)

  def update(self):
    pass

  def draw_alien(self):
    self.screen.blit(self.image, self.rect)
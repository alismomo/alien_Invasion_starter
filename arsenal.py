'''
Arsenal is there to control bullets for the ship. It knows how many bullets are there, their movement on the screen, and their deletion.
'''

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
  from alien_invasion import AlienInvasion

'''
The class keeps bullets and manage their movement.
Checks if the bullet goes off the screen to delete it.
'''
class Arsenal:
  def __init__(self, game: 'AlienInvasion'):
    self.game = game
    self.settings = game.settings
    self.arsenal = pygame.sprite.Group()

  '''
  Updates bullets
  '''
  def update_arsenal(self):
    self.arsenal.update()
    self._remove_bullets_offscreen()

  '''
  Deletes bullets that hit the top of the screen
  '''
  def _remove_bullets_offscreen(self):
    for bullet in self.arsenal.copy():
      if bullet.rect.bottom <= 0:
        self.arsenal.remove(bullet)

  '''
  Draws bullets
  '''
  def draw(self):
    for bullet in self.arsenal:
      bullet.draw_bullet()

  '''
  Creates new bullet if max amount is not reached. True if fired
  '''
  def fire_bullet(self):
    if len(self.arsenal) < self.settings.bullet_amount:
      new_bullet = Bullet(self.game)
      self.arsenal.add(new_bullet)
      return True
    return False
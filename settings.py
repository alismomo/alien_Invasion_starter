'''
Settings are responsible for storing setting for the game. It is created for easy management of the game customization
'''
from pathlib import Path

'''
Class Settings stores all the settings for the game like screen size, paths to images and sounds. 
'''
class Settings:
  def __init__(self):
    self.name: str ='Alien Invasion'
    self.screen_w = 1200
    self.screen_h = 800
    self.FPS = 60
    self.bg_file = Path.cwd() / 'Assets' / 'images' / 'blue_moon_background.png'

    self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cat_killer.png'
    self.ship_w = 40
    self.ship_h = 60
    self.ship_speed = 5

    self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'star_laser.png'
    self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'meow.ogg'
    self.bullet_speed = 7
    self.bullet_w = 50
    self.bullet_h = 80
    self.bullet_amount = 5

    self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
    self.alien_w = 40
    self.alien_h = 40
    self.fleet_speed = 2
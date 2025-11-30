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
    self.difficulty_scale = 1.1

    self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cat_killer.png'
    self.ship_w = 40
    self.ship_h = 60

    self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'star_laser.png'
    self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'meow.ogg'
    self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'bubbles-single1.wav'

    self.alien_file = Path.cwd() / 'Assets' / 'images' / 'fish_enemy.png'
    self.alien_w = 45
    self.alien_h = 45
    self.fleet_direction = 1

    self.button_w = 200
    self.button_h = 50
    self.button_color = (0, 135, 60)

    self.text_color = (255, 255, 255)
    self.button_font_size = 48
    self.HUD_font_size = 20

    self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

  def initialize_dynamic_settings(self):
    self.ship_speed = 5
    self.starting_ship_count = 3

    self.bullet_w = 50
    self.bullet_h = 80
    self.bullet_speed = 7
    self.bullet_amount = 5


    self.fleet_speed = 2
    self.fleet_drop_speed = 40

  def increase_difficulty(self):
    self.ship_speed *= self.difficulty_scale
    self.bullet_speed *= self.difficulty_scale
    self.fleet_speed *= self.difficulty_scale
    
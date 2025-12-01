from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from alien_invasion import AlienInvasion

class GameStats():
  """
  Stores game's info like score, lives, level, and high score.
  """

  def __init__(self, game: 'AlienInvasion'):
    """
    Sets starting values and loads saved high score
    """
    self.game = game
    self.settings = game.settings
    self.max_score = 0
    self.init_saved_scores()
    self.reset_stats()

  def init_saved_scores(self):
     """
     Loads saved high score from file if it exists
     """
     self.path = self.settings.scores_file
     if self.path.exists() and self.path.stat.__sizeof__() > 20:
        contents = self.path.read_text()
        scores = json.loads(contents)
        self.hi_score = scores.get('hi_score', 0)
     else:
        self.hi_score = 0
        self.save_scores()

  def save_scores(self):
     """
     Saves score to file
     """
     scores = {
        'hi_score': self.hi_score
     }
     contents = json.dumps(scores, indent=4)
     try:
        self.path.write_text(contents)
     except FileNotFoundError as e:
        print(f'File Not Found: {e}')

  def reset_stats(self):
      """
      Resets ships, level, and score when new game
      """
      self.ships_left = self.settings.starting_ship_count
      self.score = 0
      self.level = 1

  def update(self, collisions):
     """
     Updates score and checks what is new high score
     """
     self._update_score(collisions)

     self._update_max_score()

     self._update_hi_score()

  def _update_max_score(self):
      """
      Updates the max score for the current game
      """
      if self.score > self.max_score:
         self.max_score = self.score

  def _update_hi_score(self):
      """
      Updates saved high score
      """
      if self.score > self.hi_score:
         self.hi_score = self.score

  def _update_score(self, collisions):
      """
      Adds points when fish is gone
      """
      for alien in collisions.values():
         self.score += self.settings.alien_points

  def update_level(self):
     """
     Increases level number
     """
     self.level += 1
           
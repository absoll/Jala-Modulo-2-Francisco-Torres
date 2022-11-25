import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        self.name = 'bird'
        self.BIRD = BIRD
        super().__init__(self.BIRD, 0)
        self.step_index = 0
        self.rect.y = 260

    def update(self, game_speed, obstacles):
        self.type = 0 if self.step_index < 5 else 1
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0

        super().update(game_speed, obstacles)



import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactusLarge import CactusLarge
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            rand = random.randint(1,3)
            if rand == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif rand == 2:
                self.obstacles.append(CactusLarge(LARGE_CACTUS))
            elif rand == 3:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import HEART_TYPE



class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird()
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.has_power_up:
                    if game.player.type == 'hammer':                 
                        self.obstacles.remove(obstacle)
                        if obstacle.name == 'bird':
                            game.score += 30
                        elif obstacle.name == 'cactus':
                            game.score += 10
                elif game.lives > 0:
                    game.lives -= 1
                    game.player.has_power_up = True
                    game.player.type = HEART_TYPE
                    game.player.power_up_time = pygame.time.get_ticks() + 1000

                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                '''
                if not game.player.has_power_up and game.lives == 0:                   
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                elif not game.player.has_power_up and game.lives > 0:

                else:
                    if game.player.type == 'hammer':                 
                        self.obstacles.remove(obstacle)
                        if obstacle.name == 'bird':
                            game.score += 30
                        elif obstacle.name == 'cactus':
                            game.score += 10
                    elif game.player.type == 'heart':
                        game.lives -= 1
                '''
    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
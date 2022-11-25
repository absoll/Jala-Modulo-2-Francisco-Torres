import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.utils.constants import HEART_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        power_up_type =[
            Shield(),
            Hammer(),
            Heart()
        ]

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(100, 200) # 200,300
            self.power_ups.append(power_up_type[random.randint(0,2)])
            #self.power_ups.append(Shield())
            #self.power_ups.append(Hammer())

    def update(self, game):
        self.generate_power_up(game.score)

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                if power_up.type == HEART_TYPE:
                    game.lives += 1
                    self.power_ups.remove(power_up)
                else:
                    power_up.start_time = pygame.time.get_ticks()
            #        if power_up.type == 'shield':
            #            game.player.shield = True
            #        elif power_up.type == 'hammer':
            #            game.player.hammer = True
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)
                    #self.reset_power_ups(game.score)
        

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200) # 200,300
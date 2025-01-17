import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

CACTUS = [
   (LARGE_CACTUS, 300),
   (SMALL_CACTUS, 325),
]

class Cactus(Obstacle):
    def __init__(self):
        self.name = 'cactus'
        image, cactus_pos = CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos



# Antigo codigo, deve receber as imagens como parametro
'''
class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325


class CactusLarge(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 301
'''
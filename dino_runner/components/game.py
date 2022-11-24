import pygame


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.common_tasks import *
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


FONT_STYLE = "freesansbold.ttf"


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running= False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        
    def update_score(self):
        if self.playing is True:
            self.score += 1
            
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def handle_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN: # não confuda: K_DOWN
                self.game_speed = 20
                self.score = 0
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            text_image = textRender(FONT_STYLE, 22, 'Press any key to start')
            text_rect = rectPosition(text_image, half_screen_width, half_screen_height, 'center')
            self.screen.blit(text_image, text_rect) 
        else:
            death_image = textRender(FONT_STYLE, 22, f'You die {self.death_count} times :(')
            death_rect = rectPosition(death_image, half_screen_width, (half_screen_height - 150), 'center')
            self.screen.blit(death_image, death_rect)

            score_image = textRender(FONT_STYLE, 22, f'Your score was {self.score} points.')
            score_rect = rectPosition(score_image, half_screen_width, (half_screen_height - 125), 'center')
            self.screen.blit(score_image, score_rect)

            text_image = textRender(FONT_STYLE, 22, 'Press any key to restart')
            text_rect = rectPosition(text_image, half_screen_width, (half_screen_height + 150), 'center')
            self.screen.blit(text_image, text_rect)

            icon_rect = rectPosition(ICON, half_screen_width, half_screen_height, 'midbottom')
            self.screen.blit(ICON, icon_rect)

            # "Press any key to restart"
            # Mostrar Score atingido e Death_count
            # resetar game_speed e score
            # método reutilizável para desenhar os textos
            # self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))

        pygame.display.update()
        self.handle_events_menu()

import pygame
import sys
from src.the_game.backend import snake_model


class Window(object):
    SCREEN_SIZE = WIDTH, HEIGHT = (600, 600)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 50, 50)
    GREEN = (50, 255, 50)
    CIRCLE_RADIUS = 30

    def __init__(self):
        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode(Window.SCREEN_SIZE)
        pygame.display.set_caption('Press ESC to quit')
        self.fps_clocker = pygame.time.Clock()
        self.paused = False

        # Snake
        self.snake = snake_model.Snake()
        self.scale_coef = Window.WIDTH // self.snake.get_allowed_space()[1]  # 1 for y-axis

        # frames per second
        self.FPS = 30
        self.time_elapsed_since_last_action = 0
        self.clock = pygame.time.Clock()

    def __update(self):
        self.snake.move()

    def __get_pos_on_screen(self, snake_pos):
        return snake_pos * self.scale_coef + self.scale_coef // 2

    def __render(self):
        self.screen.fill(Window.BLACK)

        snake_body = self.snake.get_body_list()
        for segment in snake_body:
            x_pos = self.__get_pos_on_screen(segment[1])
            y_pos = self.__get_pos_on_screen(segment[0])
            pygame.draw.rect(self.screen, Window.GREEN,
                             (x_pos - self.scale_coef // 2,
                              y_pos - self.scale_coef // 2,
                              self.scale_coef, self.scale_coef))

        food = self.snake.get_seen_food_pos()
        x_pos = self.__get_pos_on_screen(food[1])
        y_pos = self.__get_pos_on_screen(food[0])
        pygame.draw.circle(self.screen, Window.RED,
                           [x_pos, y_pos], self.scale_coef // 2, 0)

        pygame.display.update()
        self.fps_clocker.tick(self.FPS)

    def __key_handler(self, pressed_key):
        if pressed_key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif pressed_key == pygame.K_SPACE:
            self.paused = not self.paused
        elif pressed_key == pygame.K_h:
            self.snake.turn("lt")
        elif pressed_key == pygame.K_j:
            self.snake.turn("dn")
        elif pressed_key == pygame.K_k:
            self.snake.turn("up")
        elif pressed_key == pygame.K_l:
            self.snake.turn("rt")

    def __cycle(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    self.__key_handler(event.key)

            dt = self.clock.tick()
            if not self.paused:
                self.time_elapsed_since_last_action += dt
                if self.time_elapsed_since_last_action > 250:
                    self.__update()
                    # reset it to 0 so you can count again
                    self.time_elapsed_since_last_action = 0
                self.__render()

    def run(self):
        self.__cycle()


if __name__ == "__main__":
    w = Window()
    w.run()


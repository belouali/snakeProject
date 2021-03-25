import sys
from snake import Snake
from food import Food
from score import Score
from window import Window

import pygame

import constant as c


class Game:
    def __init__(self):
        # initializing game vars
        self.game = pygame
        self.game.init()
        self.game.display.set_caption('Snake')
        # initializing all the Game objects
        self.fps = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        # making the game window appeared on the screen
        self.window = Window(self.game.display.set_mode(size=(c.WINDOW_WIDTH, c.WINDOW_HEIGHT)))

    def game_over(self):
        # snake head running into the borders of the window
        if self.snake.snake_head[0] < 0 or self.snake.snake_head[0] > c.WINDOW_WIDTH - 10:
            self.window.draw_game_over(self.game, self.exit_game)
        if self.snake.snake_head[1] < 0 or self.snake.snake_head[1] > c.WINDOW_HEIGHT - 10:
            self.window.draw_game_over(self.game, self.exit_game)

        # snake is running into itself
        for block in self.snake.snake_body[1:]:
            if block[0] == self.snake.snake_head[0] and block[1] == self.snake.snake_head[1]:
                self.window.draw_game_over(self.game, self.exit_game)

    def exit_game(self):
        self.game.quit()
        sys.exit()

    # checking if snake ate and if so, the food will reappear and score will be increased!
    def food_control(self):
        self.snake.snake_move()
        if self.snake.snake_head[0] == self.food.position[0] and self.snake.snake_head[1] == self.food.position[1]:
            self.snake.snake_grow()
            self.food.food_respawn()
            self.score.increase()

    def run(self):
        while True:
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    self.exit_game()
                elif event.type == self.game.KEYDOWN:
                    if event.key == self.game.K_ESCAPE:
                        self.exit_game()
                    else:
                        if event.key == self.game.K_DOWN or event.key == self.game.K_s:
                            self.snake.snake_change_direction('UP')
                        if event.key == self.game.K_UP or event.key == self.game.K_w:
                            self.snake.snake_change_direction('DOWN')
                        if event.key == self.game.K_LEFT or event.key == self.game.K_a:
                            self.snake.snake_change_direction('LEFT')
                        if event.key == self.game.K_RIGHT or event.key == self.game.K_d:
                            self.snake.snake_change_direction('RIGHT')

            self.food_control()
            self.game_over()
            self.window.draw_stage()
            self.window.draw_snake(self.game, self.snake.snake_body)
            self.window.draw_food(self.game, self.food.position)
            self.window.draw_score(self.game, self.score.score)
            self.game.display.update()
            self.fps.tick(20)

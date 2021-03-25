import constant as c
import time


class Window:

    def __init__(self, window):
        self.window = window

    def draw_stage(self):
        self.window.fill(c.BLACK_COLOR)

    def draw_snake(self, game, snake_body):
        for pixel in snake_body:
            game.draw.rect(self.window, c.GREEN_COLOR, game.Rect(pixel[0], pixel[1], 10, 10))

    def draw_food(self, game, food):
        game.draw.rect(self.window, c.BLUE_COLOR, game.Rect(food[0], food[1], 10, 10))

    def draw_score(self, game, score):
        score_font = game.font.SysFont('Times New Roman', 20)
        score_surface = score_font.render(f'Score: ${score}', True, c.WHITE_COLOR)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (c.WINDOW_WIDTH // 2, 15)
        self.window.blit(score_surface, score_rect)

    def draw_game_over(self, game, exit_game):
        final_font = game.font.SysFont('Comic Sans', 50)
        final_surface = final_font.render('GAME OVER', True, c.RED_COLOR)
        final_rect = final_surface.get_rect()
        final_rect.midtop = (c.WINDOW_WIDTH // 2, c.WINDOW_HEIGHT // 2)
        self.window.fill(c.BLACK_COLOR)
        self.window.blit(final_surface, final_rect)
        game.display.update()
        time.sleep(1)
        exit_game()

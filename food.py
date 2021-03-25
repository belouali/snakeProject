from random import randrange
import constant as c


class Food:
    def __init__(self):
        self.position = [100, 100]

    def food_respawn(self):
        self.position = [randrange(1, c.WINDOW_WIDTH // 10) * 10,
                         randrange(1, c.WINDOW_HEIGHT // 10) * 10]

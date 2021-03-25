
class Snake:

    def __init__(self):
        self.snake_head = [100, 50]
        self.snake_direction = 'RIGHT'
        self.snake_body = [
            self.snake_head,
            [self.snake_head[0] - 10, self.snake_head[1]],
            [self.snake_head[0] - 20, self.snake_head[1]],
        ]

    def snake_change_direction(self, new_direction: str):
        if new_direction == self.snake_direction:
            return
        if self.snake_direction == 'DOWN' and new_direction == 'UP':
            return
        if self.snake_direction == 'UP' and new_direction == 'DOWN':
            return
        if self.snake_direction == 'RIGHT' and new_direction == 'LEFT':
            return
        if self.snake_direction == 'LEFT' and new_direction == 'RIGHT':
            return
        self.snake_direction = new_direction

    def snake_move(self):
        if self.snake_direction == 'UP':
            self.snake_head = [self.snake_head[0], self.snake_head[1] + 10]
        if self.snake_direction == 'DOWN':
            self.snake_head  = [self.snake_head[0], self.snake_head[1] - 10]
        if self.snake_direction == 'RIGHT':
            self.snake_head  = [self.snake_head[0] + 10, self.snake_head[1]]
        if self.snake_direction == 'LEFT':
            self.snake_head  = [self.snake_head[0] - 10, self.snake_head[1]]
        self.snake_body.insert(0, self.snake_head)
        self.snake_body.pop()

    def snake_grow(self):
        self.snake_body.insert(0, self.snake_head)
        self.snake_move()

class Snake_control:

    def __init__(self, snake_block):
        self.snake_block = snake_block
        self.choose_head = 0


    def forward(self):
        if self.snake_block.heading() == 270 or self.choose_head == 1:
            pass
        else:
            self.snake_block.setheading(90)
            self.choose_head = 1

    def back(self):
        if self.snake_block.heading() == 90 or self.choose_head == 1:
            pass
        else:
            self.snake_block.setheading(270)
            self.choose_head = 1

    def left(self):
        if self.snake_block.heading() == 0 or self.choose_head == 1:
            pass
        else:
            self.snake_block.setheading(180)
            self.choose_head = 1

    def right(self):
        if self.snake_block.heading() == 180 or self.choose_head == 1:
            pass
        else:
            self.snake_block.setheading(0)
            self.choose_head = 1


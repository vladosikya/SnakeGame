import turtle

class Snake:
    def __init__(self):
        self.snake_train = []
        self.def_position_x = 0
        self.snake_new_block = False
        self.create_snake()

    def create_snake(self):
        for x in range(3):
            snake_block = turtle.Turtle()
            snake_block.penup()
            snake_block.shape('square')
            snake_block.color('green')
            snake_block.goto(self.def_position_x, 0)
            self.def_position_x -=20
            self.snake_train.append(snake_block)
        print("Snake created.")


    def snake_move(self):
        pos1 = self.snake_train[0].position()
        self.snake_train[0].forward(20)
        for block in self.snake_train[1:]:
            pos2 = block.position()
            block.goto(pos1)
            pos1 = pos2
        if self.snake_new_block == True:
            snake_block = turtle.Turtle()
            snake_block.penup()
            snake_block.shape('square')
            snake_block.color('green')
            snake_block.goto(pos1)
            self.snake_train.append(snake_block)
            self.snake_new_block = False
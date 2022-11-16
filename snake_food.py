import turtle, random

class Food:
    def __init__(self, screen, snake):
        self.food = turtle.Turtle()
        self.food.penup()
        self.food.shape('circle')
        self.food.color('blue')
        self.screen = screen
        self.random_position(snake)

    def random_position(self, snake):
        size = self.screen.screensize()
        xcor = size[0] / 2
        ycor = size[1] / 2
        while True:
            new_x_pos = random.randint(-xcor, xcor)
            new_y_pos = random.randint(-ycor, ycor)
            checked = 0
            need = len(snake.snake_train)
            for block in snake.snake_train:
                if block.distance(new_x_pos, new_y_pos) <= 15:
                    pass
                else:
                    checked+=1
            if checked == need:
                break
            else:
                pass



        self.food.goto(new_x_pos, new_y_pos)

    def new_food(self, snake):
        self.food.clear()
        self.random_position(snake)
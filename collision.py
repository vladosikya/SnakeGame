import turtle

class CollisionCore:
    def __init__(self):
        self.game_over = False
        self.score = 0
        try:
            with open("record.txt", "r") as file:
                best_score = file.readlines()
        except:
            with open("record.txt", "w") as file:
                best_score = []

        if best_score != []:
            self.best_score = best_score[0].strip()
        else:
            self.best_score = 0
        self.create_score()
        self.text.write(arg=f"Score: {self.score}. Record {self.best_score}", move=True, font=('Arial', 32, 'normal'), align='center')

    def create_score(self):
        self.text = turtle.Turtle()
        self.text.penup()
        self.text.goto(0, 225)
        self.text.color('white')
        self.text.hideturtle()

    def food_collision(self, snake, food):
        if snake.snake_train[0].distance(food.food.position()) <= 20:
            self.score+=1
            self.text.clear()
            self.create_score()
            self.text.write(arg=f"Score: {self.score}. Record {self.best_score}", move=True, font=('Arial', 32, 'normal'), align='center')
            snake.snake_new_block = True
            food.new_food(snake)

    def wall_collision(self, snake):
        if snake.snake_train[0].xcor() >= 340 or snake.snake_train[0].xcor() <= -340 or snake.snake_train[0].ycor() >= 300 or snake.snake_train[0].ycor() <= -300:
            self.text.clear()
            self.create_score()
            self.text.home()
            self.text.write(arg=f"Game Over!\n Score {self.score}", align='center', font=('Arial', 32, 'normal'))
            self.game_over = True

    def tail_collision(self, snake):
        head = snake.snake_train[0]
        for block in snake.snake_train[1:]:
            if block.distance(head) < 15:
                self.text.clear()
                self.create_score()
                self.text.home()
                self.text.write(arg=f"Game Over. Score {self.score}", align='center', font=('Arial', 32, 'normal'))
                self.game_over = True

    def new_record(self):
        with open('record.txt', 'w') as file:
            file.write(str(self.score))

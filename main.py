import snake_core, turtle, time, snake_control, snake_food, collision

screen = turtle.Screen()
screen.bgcolor('black')
screen.tracer(n=0)
collision_f = collision.CollisionCore()
snake = snake_core.Snake()
food = snake_food.Food(screen, snake)
control = snake_control.Snake_control(snake.snake_train[0])
screen.update()
screen.listen()


while collision_f.game_over == False:
    screen.onkey(control.forward, "Up")
    screen.onkey(control.back, "Down")
    screen.onkey(control.left, "Left")
    screen.onkey(control.right, "Right")
    snake.snake_move()
    collision_f.food_collision(snake, food)
    collision_f.wall_collision(snake)
    collision_f.tail_collision(snake)
    screen.update()
    time.sleep(0.1)
    control.choose_head = 0

collision_f.new_record()

screen.exitonclick()
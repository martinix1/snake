from turtle import *
from random import randrange, choice
from freegames import square, vector

# Lista de colores permitidos (sin rojo)
colors = ['blue', 'purple', 'orange', 'yellow', 'cyan']

# Asignar colores aleatorios distintos
snake_color = choice(colors)
food_color = choice([c for c in colors if c != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y

def inside(pos):
    """Devuelve True si la posición está dentro de los límites."""
    return -200 < pos.x < 190 and -200 < pos.y < 190

def move():
    """Mueve la serpiente un segmento hacia adelante."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()

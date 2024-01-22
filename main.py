from tkinter import *
import random

GAME_HEIGHT = 700
GAME_WIDTH = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 1
SNAKE_COLOR = "#8532a8"
FOOD_COLOR = "#f5cc02"
BACKGROUND_COLOR = "#000000"
#konstanty pro hru

class Snake():
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food():
    def __init__(self):
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE))-1) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE)-1)) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        #nahodne generovani jidla

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    #pohyb pomoci ody x, y

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
#mazani jidla a scitani skore
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
#kontrola pohybu



def check_collision(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
#kontrola narazeni hada bud do sebe samotneho nebo do okraju
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=("consolas", 70), text="Prohrál jsi!", fill="white", tags="prohra")
#vyhozeni gameover
score = 0
direction = "down"

window = Tk()
window.title("Snake Hra")
window.resizable(False, False)
window.geometry("700x700")
label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()
#nastaveni jak vypada okno, pouzit modul tkinter
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

food = Food()
snake = Snake()
#tridy do promennych
next_turn(snake, food)

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
#nabindovane tlacitka pro pohyb hada
window.mainloop()

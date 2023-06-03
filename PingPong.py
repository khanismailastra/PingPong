import random
import time
import tkinter as tk


class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.hit_bottom = False
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 512, 384)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        elif pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(500, 345, text=f"Вы проиграли!\nваш счёт: {self.score.score}",
                               font=("Ariel", 15, "bold"),
                               fill="black")
        elif self.hit_paddle(pos):
            self.y = -2
        elif pos[0] <= 0:
            self.x = 2
        elif pos[2] >= self.canvas_width:
            self.x = -2

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 200, 10, fill=color)
        self.canvas.move(self.id, 400, 600)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_right(self, event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(50, 10, text=self.score, fill=color, font=("Arial", 20))

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


root = tk.Tk()
root.title("PingPong")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = tk.Canvas(root, width=1024, height=768, bd=0, highlightthickness=0, )
canvas.pack()
root.update()
paddle = Paddle(canvas, color="black")
score = Score(canvas, "red")
ball = Ball(canvas, paddle, score, color="red")
while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    else:
        break
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
time.sleep(3)

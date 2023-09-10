import tkinter as tk
import random
import time

WIDTH, HEIGHT = 500, 500
SNAKE_length = 25
SNAKE_SPEED = 200 

class Snake_Mania:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Mania")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.generate_food()
        self.direction = "Right"
        self.score = 0

        self.root.bind("<KeyPress>", self.on_key_press)
        self.game_loop()

    def generate_food(self):
        while True:
            x = random.randint(0, (WIDTH - SNAKE_length) // SNAKE_length) * SNAKE_length
            y = random.randint(0, (HEIGHT - SNAKE_length) // SNAKE_length) * SNAKE_length
            if (x, y) not in self.snake:
                return x, y

    def on_key_press(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            new_direction = event.keysym
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if new_direction != opposite_directions.get(self.direction):
                self.direction = new_direction

    def game_loop(self):
        self.move_snake()
        self.check_collision()
        self.check_food()
        self.draw_game()

        self.root.after(SNAKE_SPEED, self.game_loop)

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= SNAKE_length
        elif self.direction == "Down":
            y += SNAKE_length
        elif self.direction == "Left":
            x -= SNAKE_length
        elif self.direction == "Right":
            x += SNAKE_length

        self.snake.insert(0, (x, y))

    def check_collision(self):
        head = self.snake[0]
        if head in self.snake[1:]:
            self.game_over()

        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT
        ):
            self.game_over()

    def check_food(self):
        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.generate_food()

    def draw_game(self):
        self.canvas.delete("all")

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + SNAKE_length, y + SNAKE_length, fill="green", outline="white"
            )

        fx, fy = self.food
        self.canvas.create_oval(
            fx, fy, fx + SNAKE_length, fy + SNAKE_length, fill="red", outline="white"
        )

        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white")

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            WIDTH // 4, HEIGHT // 4,
            text=f"Game Over\nScore: {self.score}",
            fill="white",
            font=("Arial", 26)
        )
        self.root.update()
        time.sleep(5)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = Snake_Mania(root)
    root.mainloop()



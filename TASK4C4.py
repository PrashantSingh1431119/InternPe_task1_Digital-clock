import pygame
import sys

# Constants
ROWS = 6
COLUMNS = 7
EMPTY = " "
PLAYER1 = "X"
PLAYER2 = "O"
CELL_SIZE = 80
WINDOW_WIDTH = COLUMNS * CELL_SIZE
WINDOW_HEIGHT = (ROWS + 1) * CELL_SIZE  # Extra row for dropping pieces

# Colors
GRAY = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Connect Four")

# Create the game board
board = [[EMPTY] * COLUMNS for _ in range(ROWS)]

# Function to draw the game board
def draw_board():
    for row in range(ROWS):
        for col in range(COLUMNS):
            pygame.draw.rect(window, GRAY, (col * CELL_SIZE, (row + 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if board[row][col] == PLAYER1:
                pygame.draw.circle(window, RED, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)
            elif board[row][col] == PLAYER2:
                pygame.draw.circle(window, YELLOW, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

# Function to drop a piece in a column
def drop_piece(col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return True
    return False

# Function to check for a win
def check_win(player):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (from top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (from top-right to bottom-left)
    for row in range(ROWS - 3):
        for col in range(3, COLUMNS):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True

    return False

# Main game loop
current_player = PLAYER1
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x = event.pos[0] // CELL_SIZE
            if drop_piece(x, current_player):
                if check_win(current_player):
                    game_over = True
                current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

    window.fill((0, 0, 0))
    draw_board()
    pygame.display.update()

import pygame
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650
TOP_PANEL_HEIGHT = 60
SIDE_PANEL_WIDTH = 200
BOARD_WIDTH = WINDOW_WIDTH - 2 * SIDE_PANEL_WIDTH
BOARD_HEIGHT = WINDOW_HEIGHT - TOP_PANEL_HEIGHT
CELL_SIZE = BOARD_WIDTH // 8
BOARD_X = SIDE_PANEL_WIDTH
BOARD_Y = TOP_PANEL_HEIGHT

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BG_COLOR = (50, 50, 50)

# Fonts
font = pygame.font.SysFont("Arial", 28)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Othello")

# Game title
GAME_TITLE = "*Othello*"

# Initial board setup
board = [[0 for _ in range(8)] for _ in range(8)]
board[3][3] = 2  # White
board[3][4] = 1  # Black
board[4][3] = 1  # Black
board[4][4] = 2  # White

def draw_panels():
    # Top panel
    pygame.draw.rect(screen, BG_COLOR, (0, 0, WINDOW_WIDTH, TOP_PANEL_HEIGHT))
    title_text = font.render(GAME_TITLE, True, WHITE)
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 15))

    # Left panel
    pygame.draw.rect(screen, BG_COLOR, (0, TOP_PANEL_HEIGHT, SIDE_PANEL_WIDTH, BOARD_HEIGHT))
    left_text = font.render("Left Panel", True, WHITE)
    screen.blit(left_text, (20, TOP_PANEL_HEIGHT + 20))

    # Right panel
    pygame.draw.rect(screen, BG_COLOR, (WINDOW_WIDTH - SIDE_PANEL_WIDTH, TOP_PANEL_HEIGHT, SIDE_PANEL_WIDTH, BOARD_HEIGHT))
    right_text = font.render("Right Panel", True, WHITE)
    screen.blit(right_text, (WINDOW_WIDTH - SIDE_PANEL_WIDTH + 20, TOP_PANEL_HEIGHT + 20))

def draw_grid():
    screen.fill(GREEN, rect=(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT))
    for x in range(0, BOARD_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (BOARD_X + x, BOARD_Y), (BOARD_X + x, BOARD_Y + BOARD_HEIGHT))
    for y in range(0, BOARD_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (BOARD_X, BOARD_Y + y), (BOARD_X + BOARD_WIDTH, BOARD_Y + y))

def draw_tokens():
    for row in range(8):
        for col in range(8):
            cx = BOARD_X + col * CELL_SIZE + CELL_SIZE // 2
            cy = BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2
            if board[row][col] == 1:
                pygame.draw.circle(screen, BLACK, (cx, cy), CELL_SIZE // 2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, WHITE, (cx, cy), CELL_SIZE // 2 - 5)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    draw_panels()
    draw_grid()
    draw_tokens()
    pygame.display.flip()

pygame.quit()

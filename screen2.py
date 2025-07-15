import pygame
import settings
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("./music/game music.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Othello")

font = pygame.font.SysFont(settings.FONT["name"], settings.FONT["size"])

board = [[0 for _ in range(8)] for _ in range(8)]
board[3][3], board[4][4] = 2, 2
board[3][4], board[4][3] = 1, 1
current_player = 1

def draw_panels():
    pygame.draw.rect(screen, settings.COLORS["bg"], (0, 0, settings.WINDOW_WIDTH, settings.TOP_PANEL_HEIGHT))
    title_text = font.render(settings.GAME_TITLE, True, settings.COLORS["white"])
    screen.blit(title_text, (settings.WINDOW_WIDTH // 2 - title_text.get_width() // 2, 10))

    pygame.draw.rect(screen, settings.COLORS["bg"], (0, settings.TOP_PANEL_HEIGHT, settings.SIDE_PANEL_WIDTH, settings.BOARD_HEIGHT))
    screen.blit(font.render("Player 2:", True, settings.COLORS["white"]), (20, settings.TOP_PANEL_HEIGHT + 20))

    pygame.draw.rect(screen, settings.COLORS["bg"], (settings.WINDOW_WIDTH - settings.SIDE_PANEL_WIDTH, settings.TOP_PANEL_HEIGHT, settings.SIDE_PANEL_WIDTH, settings.BOARD_HEIGHT))
    screen.blit(font.render("Player 1:", True, settings.COLORS["white"]), (settings.WINDOW_WIDTH - settings.SIDE_PANEL_WIDTH + 20, settings.TOP_PANEL_HEIGHT + 20))

def draw_grid():
    screen.fill(settings.COLORS["green"], rect=(settings.BOARD_X, settings.BOARD_Y, settings.BOARD_WIDTH, settings.BOARD_HEIGHT))
    for x in range(0, settings.BOARD_WIDTH, settings.CELL_SIZE):
        pygame.draw.line(screen, settings.COLORS["black"], (settings.BOARD_X + x, settings.BOARD_Y), (settings.BOARD_X + x, settings.BOARD_Y + settings.BOARD_HEIGHT))
    for y in range(0, settings.BOARD_HEIGHT, settings.CELL_SIZE):
        pygame.draw.line(screen, settings.COLORS["black"], (settings.BOARD_X, settings.BOARD_Y + y), (settings.BOARD_X + settings.BOARD_WIDTH, settings.BOARD_Y + y))

def draw_tokens():
    for row in range(8):
        for col in range(8):
            cx = settings.BOARD_X + col * settings.CELL_SIZE + settings.CELL_SIZE // 2
            cy = settings.BOARD_Y + row * settings.CELL_SIZE + settings.CELL_SIZE // 2
            if board[row][col] == 1:
                pygame.draw.circle(screen, settings.COLORS["black"], (cx, cy), settings.CELL_SIZE // 2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, settings.COLORS["white"], (cx, cy), settings.CELL_SIZE // 2 - 5)

def make_move(row, col, player):
    if board[row][col] != 0:
        return
    opponent = 2 if player == 1 else 1
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    board[row][col] = player
    for dx, dy in directions:
        r, c = row + dy, col + dx
        tiles_to_flip = []
        while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            tiles_to_flip.append((r, c))
            r += dy
            c += dx
        if tiles_to_flip and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
            for fr, fc in tiles_to_flip:
                board[fr][fc] = player

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            if settings.BOARD_X <= mx < settings.BOARD_X + settings.BOARD_WIDTH and settings.BOARD_Y <= my < settings.BOARD_Y + settings.BOARD_HEIGHT:
                col = (mx - settings.BOARD_X) // settings.CELL_SIZE
                row = (my - settings.BOARD_Y) // settings.CELL_SIZE
                make_move(row, col, current_player)
                current_player = 2 if current_player == 1 else 1

    draw_panels()
    draw_grid()
    draw_tokens()
    pygame.display.flip()

pygame.quit()

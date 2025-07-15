import pygame
import settings

def calculate_scores(board):
    p1_score = sum(row.count(1) for row in board)
    p2_score = sum(row.count(2) for row in board)
    return p1_score, p2_score

def draw_panels(screen, board, player1_wins, player2_wins):
    font = pygame.font.SysFont(settings.FONT["name"], settings.FONT["size"])
   

    p1_score, p2_score = calculate_scores(board)

    pygame.draw.rect(screen, settings.COLORS["bg"], (0, 0, settings.WINDOW_WIDTH, settings.TOP_PANEL_HEIGHT))
    title_text = font.render(settings.GAME_TITLE, True, settings.COLORS["green"])
    screen.blit(title_text, (settings.WINDOW_WIDTH // 2 - title_text.get_width() // 2, 10))

    pygame.draw.rect(screen, settings.COLORS["bg"], (0, settings.TOP_PANEL_HEIGHT, settings.SIDE_PANEL_WIDTH, settings.BOARD_HEIGHT))
    left_text = font.render(f"Player 2 : {p2_score}", True, settings.COLORS["white"])
    wins2_text = font.render(f"Wins: {player2_wins}", True, settings.COLORS["white"])
    screen.blit(left_text, (20, settings.TOP_PANEL_HEIGHT + 20))
    screen.blit(wins2_text, (20, settings.TOP_PANEL_HEIGHT + 70))

    pygame.draw.rect(screen, settings.COLORS["bg"], (settings.WINDOW_WIDTH - settings.SIDE_PANEL_WIDTH, settings.TOP_PANEL_HEIGHT, settings.SIDE_PANEL_WIDTH, settings.BOARD_HEIGHT))
    right_text = font.render(f"Player 1 : {p1_score}", True, settings.COLORS["red"])
    wins1_text = font.render(f"Wins: {player1_wins}", True, settings.COLORS["red"])
    screen.blit(right_text, (settings.WINDOW_WIDTH - settings.SIDE_PANEL_WIDTH + 20, settings.TOP_PANEL_HEIGHT + 20))
    screen.blit(wins1_text, (settings.WINDOW_WIDTH - settings.SIDE_PANEL_WIDTH + 20, settings.TOP_PANEL_HEIGHT + 70))

def draw_winner(screen, board):
    font = pygame.font.SysFont(settings.FONT["name"], settings.FONT["size"])
    

    p1_score, p2_score = calculate_scores(board)
    if p1_score > p2_score:
        message = "Player 1 Wins!"
        color = (255, 215, 0)
        text = font.render(message, True, color)
        screen.blit(text, (settings.WINDOW_WIDTH - text.get_width() - 10, 10))
    elif p2_score > p1_score:
        message = "Player 2 Wins!"
        color = (255, 215, 0)
        text = font.render(message, True, color)
        screen.blit(text, (10, 10))
    else:
        message = "It's a Draw!"
        color = (0, 255, 255)
        text = font.render(message, True, color)
        screen.blit(text, (10, 10))
        screen.blit(text, (settings.WINDOW_WIDTH - text.get_width() - 10, 10))

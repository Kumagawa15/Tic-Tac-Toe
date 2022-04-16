import pygame
from container import BOARD_ROWS, BOARD_COLS, CIRCLE_COLOR, CIRCLE_RADIUS, CIRCLE_WIDTH, CROSS_COLOR, CROSS_WIDTH,SPACE, TRIANGLE_COLOR, TRIANGLE_WIDTH

class Figure:
    def draw_figures(self, boardMark, screen):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if boardMark[row] [col] == 1:
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 150 + 75), int(row * 150 + 75)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif boardMark[row] [col] == 2:
                    pygame.draw.line(screen, CROSS_COLOR, (col * 150 + SPACE, row * 150 + 150 - SPACE), (col * 150 + 150 - SPACE, row * 150 + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * 150 + SPACE, row * 150 + SPACE), (col * 150 + 150 - SPACE, row * 150 + 150 - SPACE), CROSS_WIDTH)
                elif boardMark[row] [col] == 3:
                    pygame.draw.line(screen, TRIANGLE_COLOR, (col * 150 + SPACE, row * 150 + 150 - SPACE), (col * 150 + 45 + SPACE, row * 150 + SPACE), TRIANGLE_WIDTH)
                    pygame.draw.line(screen, TRIANGLE_COLOR, (col * 150 + 150 - SPACE, row * 150 + 150 - SPACE), (col * 150 + 45 + SPACE, row * 150 + SPACE), TRIANGLE_WIDTH)
                    pygame.draw.line(screen, TRIANGLE_COLOR, (col * 150 + SPACE, row * 150 + 150 - SPACE), (col * 150 + 150 - SPACE, row * 150 + 150 - SPACE), TRIANGLE_WIDTH)
import pygame
from container import WIDTH, HEIGHT, BG_COLOR, LINE_COLOR, LINE_WIDTH

class Board:
    def __init__(self):
        #Mmebuat layar dengan ukuran 600x600
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #Pemberian warna backgroun layar
        self.screen.fill(BG_COLOR)
        #Pemanggilan method draw_line
        self.draw_line() 

    def draw_line(self):
        #Horizontal Line 1 
        pygame.draw.line(self.screen, LINE_COLOR, (0, 150), (600, 150), LINE_WIDTH)
        #Horizontal Line 2
        pygame.draw.line(self.screen, LINE_COLOR, (0, 300), (600, 300), LINE_WIDTH)
        #Horizontal Line 3
        pygame.draw.line(self.screen, LINE_COLOR, (0, 450), (600, 450), LINE_WIDTH)

        #Vertikal Line 1
        pygame.draw.line(self.screen, LINE_COLOR, (150, 0), (150, 600), LINE_WIDTH)
        #Vertikal Line 2
        pygame.draw.line(self.screen, LINE_COLOR, (300, 0), (300, 600), LINE_WIDTH)
        #Vertikal Line 3
        pygame.draw.line(self.screen, LINE_COLOR, (450, 0), (450, 600), LINE_WIDTH)
    
    
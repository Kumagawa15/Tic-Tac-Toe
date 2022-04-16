
import pygame, sys

from board import Board
from game import Game
from figure import Figure

#pemberian nama caption layar
pygame.display.set_caption('TIC TAC TOE')
board = Board()
game = Game()
figure = Figure()
#kondisi false jika game over
gameOver = False

while True:
    #looping untuk layar agar tidak close saat di run 
    for event in pygame.event.get():
        #kondisi untuk menghentikan game
        if event.type == pygame.QUIT:
            sys.exit()

        #kondisi saat pemencetan atau pengklikkan mouse
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                #penentuan posisi x dan y yang mengikut arah pengklikan mouse
                mouseX = event.pos[0] #X
                mouseY = event.pos[1] #Y

                #penentuan posisi pengklikan mouse untuk setiap kolum dan baris
                clicked_row = int(mouseY // 150)
                clicked_col = int(mouseX // 150)

                #kondisi untuk pengecekan apakah kotak masih tersedia,
                #dengan kolum dan baris yang ditentukan oleh pengklikan mouse
                if game.availabale_square(clicked_row, clicked_col):
                    #kondisi jika player 1 jalan
                    if game.player == 1:
                        #pembuatan penanda untuk player 1
                        game.mark_square(clicked_row, clicked_col, 1)
                        #kondisi jika player 1 menang
                        if game.check_win(game.player, board.screen):
                            #menghentikan permainan (tidak keluat dari layar)
                            gameOver = True
                        #melanjutkan urutan main ke player 2
                        game.player = 2 
                    elif game.player == 2:
                        game.mark_square(clicked_row, clicked_col, 2)
                        if game.check_win(game.player, board.screen):
                            gameOver = True
                        game.player = 3
                    elif game.player == 3:
                        game.mark_square(clicked_row, clicked_col, 3)
                        if game.check_win(game.player, board.screen):
                            gameOver = True
                        game.player = 1

                    #pemanggilan fungsi pengambaran simbol untuk pemain beserta pengambilan atribut yang diperlukan
                    figure.draw_figures(game.boardMark, board.screen)

        #kondisi jika pemain menekan keyboard
        if event.type == pygame.KEYDOWN:
            #kondisi jika key K pada keyboard ditekan
            if event.key == pygame.K_r:
                #memanggil fungsi restrat beserta pengambilan atribut yang diperlukan 
                game.restart(board.screen, board.draw_line)
                #lalu mengulang kondisi awal objek player menjadi 1
                game.player = 1
                #permainan bisa dilakukan kembali 
                gameOver = False

    #melakukan update pada layar
    pygame.display.update()
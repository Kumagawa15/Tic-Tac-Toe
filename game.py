import pygame
import numpy as np
from container import BOARD_ROWS, BOARD_COLS, HEIGHT, WIDTH, CIRCLE_COLOR, CROSS_COLOR, TRIANGLE_COLOR, BG_COLOR

class Game:
    def __init__(self):
        #Pembuatan multidemensional array dengan isi array 0 semua (tidak memiliki nilai karena menggunakan np.zero) 
        self.boardMark = np.zeros((BOARD_ROWS, BOARD_COLS))
        #objek payer(pemain)
        self.player = 1
    
    #Menandai kotak yang ditepati oleh pemain yang jalan 
    def mark_square(self, row, col, player):
        self.boardMark[row] [col] = player

    #Mengecek kota-kota yang belum ditempati dan sudah ditempati
    def availabale_square(self, row, col):
        #mengembalikan kondisi jika sudah mengecek colum dan baris (keadaan False)
        if self.boardMark[row] [col] == 0:
            #Belum ditempati
            return True
        else:
            #sedah ditempati
            return False   

    #pengecekan terhadap semua kotak (sudah penuh atau belum)
    def is_board_full(self):
        #melakukan perulangan kembali(keadaan False)
        #melakukan looping untuk setiap kolum dan baris
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                #kondisi jika kolum dan baris kosong
                if self.boardMark[row] [col] == 0:
                    #mengembalikan perulamngan ketika belum terisi semua
                    return False

        return True

    #Pengecekan keadaan menang
    def check_win(self, player, screen):
        #Vertical Win Check
        #Melakukan looping terhadap colum yang berukuran 4
        for col in range(BOARD_COLS):
            #(kondisional)jika setiap baris dari 0 samapi 3 beserta kolum yang sejajar dengan barisnya memiliki nilai player yang sama
            if self.boardMark[0][col] == player and self.boardMark[1][col] == player and self.boardMark[2][col] == player and self.boardMark[3][col] == player:
                #maka pemanggilan ini dilakuakn beserta pengambilan nilai player dan colum
                self.draw_vertical_winning_line(col, player, screen)
                #mengembalikan nilai True agar looping berhenti
                return True

        #Horizontal Win Check
        #Melakukan looping terhadap baris yang berukuran 4
        for row in range(BOARD_COLS):
            #(kondisional)jika setiap kolum dari 0 samapi 3 beserta baris yang sejajar dengan kolumnya memiliki nilai player yang sama
            if self.boardMark[row][0] == player and self.boardMark[row][1] == player and self.boardMark[row][2] == player and self.boardMark[row][3] == player:
                #maka pemanggilan ini dilakuakn beserta pengambilan nilai player dan baris
                self.draw_horizontal_winning_line(row, player, screen)
                #mengembalikan nilai True agar looping berhenti
                return True

        #Asc Diagonal Win check
        #(kondisional)jika letak posisi kolum dan baris sesuai dengan yang ada dibawah dan nilai playernya sama
        if self.boardMark[0][3] == player and self.boardMark[1][2] == player and self.boardMark[2][1] == player and self.boardMark[3][0] == player:
            #maka pemanggilan ini dilakuakn beserta pengambilan nilai player 
            self.draw_asc_diagonal(player, screen)
            #mengembalikan nilai True karena kondisi ini sudah selesai
            return True

        #Dasc Diagonal Win check
        #(kondisional)jika letak posisi kolum dan baris sesuai dengan yang ada dibawah dan nilai playernya sama
        if self.boardMark[0][0] == player and self.boardMark[1][1] == player and self.boardMark[2][2] == player and self.boardMark[3][3] == player:
            #maka pemanggilan ini dilakuakn beserta pengambilan nilai player 
            self.draw_desc_diagonal(player, screen)
            #mengembalikan nilai True karena kondisi ini sudah selesai
            return True 

    #pembuatan line vertikal yang menang
    def draw_vertical_winning_line(self, col, player, screen):
        #rumus untuk menentukan posisi x
        posX = col * 150 + 75

        #pemberian nilai untuk pemain beserta pemberian warna line yang mengikuti warna simbol
        if player == 1:
            color = CIRCLE_COLOR
        if player == 2:
            color = CROSS_COLOR
        if player == 3:
            color = TRIANGLE_COLOR

        #pembuatan line 
        pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15) 

    #pembuatan line horizontal yang menang
    def draw_horizontal_winning_line(self, row, player, screen):
        #rumus untuk menentukan posisi y
        posY = row * 150 + 75

        #pemberian nilai untuk pemain beserta pemberian warna line yang mengikuti warna simbol
        if player == 1:
            color = CIRCLE_COLOR
        if player == 2:
            color = CROSS_COLOR
        if player == 3:
            color = TRIANGLE_COLOR

        #pembuatan line 
        pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15) 

    #pembuatan line diagonal dari atas kanan sanpai bawah kiri  yang menang
    def draw_asc_diagonal(self, player, screen):
        #pemberian nilai untuk pemain beserta pemberian warna line yang mengikuti warna simbol
        if player == 1:
            color = CIRCLE_COLOR
        if player == 2:
            color = CROSS_COLOR
        if player == 3:
            color = TRIANGLE_COLOR

        #pembuatan line 
        pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15) 

    #pembuatan line diagonal dari atas kiri sanpai bawah kana  yang menang
    def draw_desc_diagonal(self, player, screen):
        #pemberian nilai untuk pemain beserta pemberian warna line yang mengikuti warna simbol
        if player == 1:
            color = CIRCLE_COLOR
        if player == 2:
            color = CROSS_COLOR
        if player == 3:
            color = TRIANGLE_COLOR

        #pembuatan line 
        pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

    #melakukan restart pada permainan
    def restart(self, screen, draw_line):
        #jika terjadi restart membuat papan kembali denga warna papan beserta garis yang akan membentuk kota
        screen.fill(BG_COLOR)
        draw_line()
        #malakukan looping dan menghasilkan semua nilai kolum dan basri 0
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                self.boardMark[row][col] = 0

        
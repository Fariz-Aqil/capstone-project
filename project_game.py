import pygame
import random


pygame.init()

# bagian display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game with Menu')

# warna yang digunakan
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)

#pengaturan kecepatan dan ukuran ular
snake_block = 10
snake_speed = 20

# inisialisasi clock dan font
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# fungsi untuk menggambar ular
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

# fungsi untuk menampilkan pesan
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(mesg, mesg_rect)

def message_center(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(mesg, mesg_rect)

# fungsi untuk menampilkan skor
def show_score(score):
    value = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(value, [0, 0])

# tampilan menu game
def game_menu():
    menu = True
    while menu:
        screen.fill(white)
        message("Welcome to Snake Game!", black)
        # Geser tulisan ke bawah dengan membuat fungsi message_below
        def message_below(msg, color, y_offset=100):
            mesg = font_style.render(msg, True, color)
            mesg_rect = mesg.get_rect(center=(screen_width // 2, screen_height // 3 + y_offset))
            screen.blit(mesg, mesg_rect)
        message_below("Press S to Start or Q to Quit", red, 80)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    menu = False

# fungsi utama untuk menjalankan game
def gameLoop():
    game_over = False
    game_close = False
    score = 0

# posisi awal ular
    x1 = 300
    y1 = 300

    x1_change = 0
    y1_change = 0

# daftar untuk menyimpan posisi ular
    snake_List = []
    Length_of_snake = 1

# posisi makanan
    foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0

# loop utama game jika game over
    while not game_over:

        while game_close == True:
            screen.fill((0, 0, 0))
            message(f"Score: {score}", (255, 255, 0))
            message_center("Kamu kalah, coba lagi! (C = Ulang, esc = Keluar)", (255, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

# control game di input dari keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
                
    # cek jika ular keluar dari layar
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

    # update posisi ular
        x1 += x1_change
        y1 += y1_change
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

    # cek jika ular menabrak dirinya sendiri
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

    # memanggil ular dan skor
        our_snake(snake_block, snake_List)
        show_score(score)

        pygame.display.update()

    # cek jika ular memakan makanan
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

        pygame.display.update()

        clock.tick(snake_speed)

    # keluar dari game
    pygame.quit()
    quit()
    
# menjalankan game
game_menu()
gameLoop()
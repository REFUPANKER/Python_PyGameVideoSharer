import pygame
import numpy as np
import random
from moviepy.editor import ImageSequenceClip

def Run():
    print("Starting game")
    # Pygame'i başlat
    pygame.init()

    # Pencere boyutları
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ball Bounce Pygame to Video")

    # Renkler
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Top özellikleri
    ball_radius = 20
    ball_color = white
    speedScale = 5
    ball_speed = [random.choice([-speedScale, speedScale])*2, random.choice([-speedScale, speedScale])]
    ball_pos = [width//2, height // 2]

    # Yazı tipi ayarları
    font = pygame.font.Font(None, 36)  # Varsayılan yazı tipi ve boyut

    

    # Oyun durumu
    running = True
    finished = False

    # Kareleri depolamak için liste
    frames = []

    # Ana oyun döngüsü
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    bounces = 0
    max_bounces = 30
    bounceLabelColor = (45, 45, 45)
    max_time = 10
    progressBarSize = 10

    lineMovement = 0
    lineWidth = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Oyun belirli çarpma sonucu veya 60 saniye sonra  bitsin
        if ((pygame.time.get_ticks() - start_ticks) / 1000.0 >= max_time):
            finished = True
            running = False

        # Topun konumunu güncelle
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Topun duvarlara çarpıp çarpmadığını kontrol et ve yönünü değiştir
        if ball_pos[0] <= ball_radius or ball_pos[0] >= width - ball_radius:
            ball_speed[0] = -ball_speed[0]
            bounces += 1
            bounceLabelColor = (random.randint(45, 255), random.randint(
                45, 255), random.randint(45, 255))

        if ball_pos[1] <= ball_radius or ball_pos[1] >= height - ball_radius:
            ball_speed[1] = -ball_speed[1]
            bounces += 1
            bounceLabelColor = (random.randint(45, 255), random.randint(
                45, 255), random.randint(45, 255))

        # Ekranı siyah ile doldur
        screen.fill(black)

        # Çarpma sayısını ekrana yazdır
        bounceStrLen = len(str(bounces))
        bounceLabelSize = int((width*((10-bounceStrLen)*10))/100)
        font_large = pygame.font.Font(None, bounceLabelSize)
        text1 = font_large.render(f"{bounces}", True, bounceLabelColor)
        text_rect1 = text1.get_rect(center=(width / 2-(bounceStrLen/2), height/2))
        screen.blit(text1, text_rect1)

        # Çizgileri ve topu çiz
        if lineMovement > width:
            lineMovement = 0

        pygame.draw.line(screen, "#43e851", [lineMovement, 0], ball_pos, lineWidth)
        pygame.draw.line(screen, "#43e851", [0, height-lineMovement], ball_pos, lineWidth)
        pygame.draw.line(screen, "#43e851", [width, lineMovement], ball_pos, lineWidth)
        pygame.draw.line(screen, "#43e851", [width-lineMovement, height], ball_pos, lineWidth)
        lineMovement += 1

        pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

        # draw progress
        MinuteProgress = (pygame.time.get_ticks()-start_ticks)/1000
        pygame.draw.line(screen, (173, 173, 173), [0, height-progressBarSize/2],
                         [(width*MinuteProgress)/max_time, height-progressBarSize/2], progressBarSize)

        # Pygame ekranını güncelle
        pygame.display.flip()

        # Ekran görüntüsünü al
        frame = pygame.surfarray.array3d(screen)
        # Pygame'den alınan görüntünün eksenlerini düzelt
        frame = np.transpose(frame, (1, 0, 2))
        frames.append(frame)

        clock.tick(60)

    # Pygame'i kapat
    pygame.quit()

    # Görüntüleri videoya dönüştür
    clip = ImageSequenceClip(frames, fps=60)
    clip.write_videofile("ballbounce.mp4", codec="libx264")
    print("Game ended")

if __name__=="__main__":
    Run()
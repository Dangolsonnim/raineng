import pygame
import random
import sys

# 1. 게임 초기화 및 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 폰트 설정
font = pygame.font.SysFont('samsungsharpsans', 40)
small_font = pygame.font.SysFont('samsungsharpsans', 30)

# 2. 단어 목록 불러오기
try:
    with open("words.txt", "r") as f:
        words = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print("오류: 'words.txt' 파일을 찾을 수 없습니다.")
    sys.exit()

# 3. 게임 변수 초기화
score = 0
current_word = random.choice(words)
typed_word = ""
word_x = random.randint(50, WIDTH - 200)
word_y = 0
word_speed = 3

# 4. 게임 루프
running = True
while running:
    # 5. 이벤트 처리 (키보드 입력, 종료)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                typed_word = typed_word[:-1]
            elif event.key == pygame.K_RETURN: # Enter 키를 누르면
                if typed_word == current_word:
                    score += 10
                    # 새 단어 생성
                    current_word = random.choice(words)
                    typed_word = ""
                    word_y = 0
                    word_x = random.randint(50, WIDTH - 200)
            else:
                typed_word += event.unicode

    # 6. 게임 로직 (단어 아래로 이동)
    word_y += word_speed
    if word_y > HEIGHT: # 단어가 바닥에 닿으면
        current_word = random.choice(words)
        typed_word = ""
        word_y = 0
        word_x = random.randint(50, WIDTH - 200)

    # 7. 화면 그리기
    screen.fill(BLACK)
    
    # 떨어지는 단어 그리기
    word_surface = font.render(current_word, True, WHITE)
    screen.blit(word_surface, (word_x, word_y))
    
    # 입력 중인 단어 그리기
    typed_surface = font.render(typed_word, True, RED)
    pygame.draw.rect(screen, WHITE, (50, HEIGHT - 70, WIDTH - 100, 50), 2)
    screen.blit(typed_surface, (60, HEIGHT - 65))
    
    # 점수 그리기
    score_surface = small_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
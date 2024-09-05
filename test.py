import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("숫자 1 입력 처리")

# 폰트 설정
font = pygame.font.Font(None, 40)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키보드 입력 처리
        if event.type == pygame.KEYDOWN:
            # 숫자 1 키를 입력했을 때의 기능
            if event.key == pygame.K_1:
                print("숫자 1이 입력되었습니다! 원하는 기능을 수행합니다.")

    # 화면 배경을 흰색으로 채우기
    screen.fill((255, 255, 255))

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()

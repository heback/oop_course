import pygame
import random

# 초기화
pygame.init()

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Shooter")

# 클래스 정의
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 25))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT-30))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)
        all_sprites.add(bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), 0))
        self.speed = random.randint(1, 3)
        self.shoot_delay = 2000  # 2초마다 무기 발사
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            enemy_bullets.add(bullet)
            all_sprites.add(bullet)
            self.last_shot = now

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill()
        self.shoot()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.move_ip(0, -5)
        if self.rect.bottom < 0:
            self.kill()


class EnemyBullet(Bullet):
    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > HEIGHT:
            self.kill()


player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont(None, 36)  # 점수 표시용 폰트

enemy_bullets = pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    screen.fill(WHITE)

    player.move()

    if random.random() < 0.02:
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    # 플레이어와 적의 충돌 검사
    if pygame.sprite.spritecollideany(player, enemies):
        running = False

    # 플레이어와 적의 무기 충돌 검사
    if pygame.sprite.spritecollideany(player, enemy_bullets):
        running = False

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    # 점수 표시
    score_display = font.render(str(score), True, BLACK)
    screen.blit(score_display, (WIDTH - 50, 10))

    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

from pygame import*
from random import*

font.init()
font = font.Font(None, 40)
win_width = 800
win_height = 600
left_bound = 100
right_bound = 550
shift = 0

img_file_back = 'cave.png'
img_file_hero = 'm1.png'
img_file_enemy = 'enemy.png'
img_file_bomb = 'bomb.png'
img_file_princess = 'princess.png'

C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(image1), (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Hero(GameSprite):
    def __init__(self, image1, x, y):
        GameSprite.__init__(self, image1, x, y)
        self.x_speed = 0
        self.y_speed = 0
        self.stands_on = False

    def gravitate(self):
        self.y_speed += 0.25

    def jump(self):
        if self.stands_on:
            self.y_speed = -7

    def update(self):

        self.rect.x += self.x_speed
        platforms = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms:
                self.rect.left = max(self.rect.left, p.rect.right)


        self.gravitate()
        self.rect.y += self.y_speed
        platforms = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                    self.stands_on = True
        elif self.y_speed < 0:
            self.stands_on = False
            for p in platforms:
                self.y_speed = 0
                self.rect.top = p.rect.bottom

class Wall(sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
        sprite.Sprite.__init__(self)
        self.image = Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(GameSprite):
    def update(self):
        self.rect.x += randint(-5, 5)
        self.rect.y += randint(-5, 5)

window = display.set_mode((800, 600))
background = transform.scale(image.load(img_file_back), (800,600))

all_sprites = sprite.Group()
barriers = sprite.Group()
enemies = sprite.Group()
bombs = sprite.Group()

robin = Hero(img_file_hero, 50, 10)

w1 = Wall(50, 150, 480, 20)
w2 = Wall(700, 150, 50, 260)
w3 = Wall(350, 380, 640, 20)
w4 = Wall(-200, 570, 1600, 20)

en1 = Enemy(img_file_enemy, 50, 480)
en2 = Enemy(img_file_enemy, 400, 480)

bomb = Enemy(img_file_bomb, 550, 400)

finish = GameSprite(img_file_princess, 1000, 450)
finish.image = transform.scale(finish.image, (60, 120))

all_sprites.add(robin, w1, w2, w3, w4, en1, en2, finish)
barriers.add(w1, w2, w3, w4)
enemies.add(en1, en2)
bombs.add(bomb)

run = True
while run:
    if (
        robin.rect.x > right_bound and robin.x_speed > 0
        or
        robin.rect.x < left_bound and robin.x_speed < 0
    ):
        shift -= robin.x_speed
        for s in all_sprites:
            s.rect.x -= robin.x_speed
        for s in bombs:
            s.rect.x -= robin.x_speed
    local_shift = shift % win_width
    window.blit(background, (local_shift, 0))
    if local_shift != 0:
        window.blit(background, (local_shift - win_width, 0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                robin.x_speed = -5
            if e.key == K_RIGHT:
                robin.x_speed = 5
            if e.key == K_UP:
                robin.jump()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                robin.x_speed = 0
            if e.key == K_RIGHT:
                robin.x_speed = 0
    all_sprites.update()
    all_sprites.draw(window)
    bombs.draw(window)

    if sprite.spritecollide(robin, enemies, False) or sprite.spritecollide(robin, bombs, False) or robin.rect.top > win_height:
        run = False
        window.fill(C_BLACK)
        text = font.render("GAME OVER", 1, C_RED)
        window.blit(text, (300, 250))

    sprite.groupcollide(all_sprites, bombs, True, True)

    if sprite.collide_rect(robin, finish):
        run = False
        window.fill(C_BLACK)
        text = font.render("YOU WIN", 1, C_RED)
        window.blit(text, (300, 250))

    display.update()
time.delay(500)

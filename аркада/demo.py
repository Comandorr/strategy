from pygame import*
from random import*
window = display.set_mode((800, 600))
background = image.load('cave.png')
background = transform.scale(background, (800, 600))
window.blit(background, (0, 0))


class MainSprite(sprite.Sprite):
   def __init__(self, image1, x, y, speed = 5, width = 70, height = 70):
       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(image1), (width, height))
       self.speed = speed

       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        sprite.Sprite.__init__(self)
        self.image = Surface([width, height])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

class Enemy(MainSprite):
    def update(self):
        self.rect.x = self.rect.x + randint(-12, 12)
        self.rect.y = self.rect.y + randint(-12, 12)

class Player(MainSprite):
    def __init__(self, image1, x, y, speed = 5, width = 70, height = 70):
        MainSprite.__init__(self, image1, x, y, speed = 5, width = 70, height = 70)
        self.x_speed = 0
        self.y_speed = 0
        self.stands_on = False

    def gravitate(self):
        self.y_speed = self.y_speed + 0.25

    def jump(self):
        if self.stands_on:
            self.y_speed = -7

    def update(self):
        #горизонтальное движение
        self.rect.x += self.x_speed
        platforms = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for p in platforms:
                self.rect.right = min(self.rect.right, p.rect.left)

        if self.x_speed < 0:
            for p in platforms:
                self.rect.left = max(self.rect.left, p.rect.right)

        #вертикальное движение
        self.gravitate()
        self.rect.y += self.y_speed
        platforms = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for p in platforms:
                self.y_speed = 0
                if self.rect.bottom > p.rect.top:
                    self.rect.bottom = p.rect.top
                    self.stands_on = True

        if self.y_speed < 0:
            self.stands_on = False
            for p in platforms:
                self.y_speed = 0
                self.rect.top = p.rect.bottom


player1 = Player("m1.png", 100, 25)
w1 = Wall(50, 100, 200, 20)
enemy = Enemy("enemy.png", 200, 100)
all_sprites = sprite.Group()
all_sprites.add(player1, w1, enemy)

walls = sprite.Group()
walls.add(w1)

run = True
while run:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                player1.x_speed = 5
            if e.key == K_LEFT:
                player1.x_speed = -5
            if e.key == K_SPACE:
                player1.jump()
        if e.type == KEYUP:
            if e.key == K_RIGHT:
                player1.x_speed = 0
            if e.key == K_LEFT:
                player1.x_speed = 0
        if e.type == QUIT:
            run = False

    window.blit(background, (0, 0))

    all_sprites.update()
    all_sprites.draw(window)



    display.update()

time.delay(1000)

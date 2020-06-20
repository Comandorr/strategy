from pygame import*
from random import*
window = display.set_mode((800, 600))
background = image.load('cave.png')
background = transform.scale(background, (800, 600))
window.blit(background, (0, 0))


class MainSprite(sprite.Sprite):
   def __init__(self, image1, x, y, speed = 5, width = 70, height = 70):
       sprite.Sprite.__init__(self)

       self.image = image1
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

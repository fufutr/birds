from cmath import rect
import pygame, sys
from pygame.locals import *

pantalla_X = 350
pantalla_Y = 1300
#CLASE FUNDO#
class Fundo(pygame.sprite.Sprite):
     def __init__(self):
         super().__init__()
         self.image = pygame.image.load("forest.jpg")
         self.rect = self.image.get_rect(center = (pantalla_X, pantalla_Y))
         #self.rect.topright = [x_pos]
         #self.rect = pygame.Rect(yy,xx,0,0)


     def update(self):
         
         self.rect.center = pos


 #CLASE PAJAROS#        
class Pajaro(pygame.sprite.Sprite):
    def __init__(self,Xpos,Ypos):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("aves_sprite/(0_0).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_1).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_2).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_3).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_4).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_5).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_6).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_7).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_8).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_9).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_10).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_11).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_12).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_13).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_14).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_15).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_16).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_17).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_18).png"))
        self.sprites.append(pygame.image.load("aves_sprite/(0_19).png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [Xpos, Ypos]

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



pygame.init()
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
speed = 10
xx = (-500)
yy = (-400)
keys = pygame.key.get_pressed()
blanco = (255, 255, 255)
negro = (0, 0, 0)
azul = (150, 10, 10)
pantalla = pygame.display.set_mode((pantalla_Y, pantalla_X))
pygame.display.set_caption(("aves1.0"))
#pantalla.fill((blanco))





#GRUPOS#
fundo = Fundo()
fundo_group = pygame.sprite.Group()
fundo_group.add(fundo)

Xpos = (100)
Ypos = (100)
aves = Pajaro(Xpos, Ypos)
aves_group = pygame.sprite.Group()
aves_group.add(aves) 


while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame = quit()
        elif event.type == MOUSEWHEEL:
            event.flipped = True
            print(event)
            print(event.x, event.y)
            print(event.flipped)
          # print(event.which)
    
    
    
    pos = pygame.mouse.get_pos()
    print(pos)
    xxx = 0
    yyy = 0
    if pos >= (900,10) or pos <= (150,10):
        pygame.time.delay(10)
        pygame.mouse.set_pos(900,100)
        
    #print(otro)

    roda = pygame.MOUSEWHEEL
    #print(roda)
    
    keys = pygame.key.get_pressed()
    if keys [pygame.K_s]:
     yy += speed
     print(yy)



    fundo_group.draw(pantalla)
    fundo_group.update()

    aves_group.draw(pantalla)
    aves_group.update()

    pygame.display.flip()
    pygame.display.update()
  #  pantalla.blit()
    clock.tick(20)    
import pygame
import random
import os


class Slime(pygame.sprite.Sprite):
    def __init__(self):
        self.image_adress = os.path.join('Images', 'SlimeS.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (50, 50))
        self.x = 50
        self.y = 50
        self.delta = 1
        self.pos = 50, 50
        self.iss = True
      
    def move(self, pos):
        if (pos != self.pos) or self.iss == True:
            self.pos = pos
            if (self.pos[0] - self.x)!=0:
                if self.x-self.pos[0] < 0:
                    self.iss = True
                    self.image_adress = os.path.join('Images', 'SlimeR.png')
                    self.my_image = pygame.image.load(self.image_adress).convert_alpha()
                    self.my_image = pygame.transform.scale(self.my_image, (50, 50))
                    self.x+=self.delta
                else:
                    self.image_adress = os.path.join('Images', 'SlimeL.png')
                    self.my_image = pygame.image.load(self.image_adress).convert_alpha()
                    self.my_image = pygame.transform.scale(self.my_image, (50, 50))
                    self.x-=self.delta
                    self.iss = True
            else:
                if (self.pos[1]- self.y)!=0:
                    if (self.y-self.pos[1]) < 0:
                        self.image_adress = os.path.join('Images', 'SlimeFB.png')
                        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
                        self.my_image = pygame.transform.scale(self.my_image, (50, 50))
                        self.y+=1
                        self.iss = True
                    elif (self.y-self.pos[1]) > 0:
                        self.image_adress = os.path.join('Images', 'SlimeFB.png')
                        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
                        self.my_image = pygame.transform.scale(self.my_image, (50, 50))
                        self.y-=1
                        self.iss = True
                else:
                    self.iss = False
                    self.image_adress = os.path.join('Images', 'SlimeS.png')
                    self.my_image = pygame.image.load(self.image_adress).convert_alpha()
                    self.my_image = pygame.transform.scale(self.my_image, (50, 50))
    
    def get(self):
        return self.iss

    def draw(self, screen):
        screen.blit(self.my_image,(self.x-25, self.y-25))


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image_adress = os.path.join('Images', 'Field.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.a = 60
        self.my_image = pygame.transform.scale(self.my_image, (self.a, self.a))
        self.x = x
        self.y = y
        self.li = ['B', 'G', 'Y', 'P', 'D', 'R']
        self.ind = -1
        self.rect = pygame.Rect(self.x, self.y, self.a, self.a)

    def change(self):
        if self.ind>=(len(self.li)-1):
            self.ind = 0
        else:
            self.ind+=1
        self.image_adress = os.path.join('Images', f'Field{self.li[self.ind]}.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (self.a, self.a))
    
    def draw(self, screen):
        screen.blit(self.my_image,(self.x, self.y))


import pygame
import random
import objects


WIDTH = 600
HEIGHT = 600


pygame.display.set_caption("Slime")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
list_f = []
for i in range(0,10):
    for j in range(0,10):
        list_f.append(objects.Field(i*60, j*60))
slime = objects.Slime()



done = False
get = False
col = None
pos = 100, 100


while not done:
    screen.fill((0,0,0))   
    clock.tick(60)
    

    for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = True
            if pygame.mouse.get_pressed()[0] == 1  and get == False:
                if pygame.mouse.get_pos()[0] in range(0,601) and pygame.mouse.get_pos()[1] in range(0,601):
                    for i in range(len(list_f)):
                        pos = pygame.mouse.get_pos()
                        if list_f[i].rect.collidepoint(pos):
                            
                            get = True
                            col = i
                            
                                          
    for i in list_f:
        i.draw(screen)


    slime.draw(screen)
    if get == True:
        slime.move(    (int (pos[0]),  int (pos[1])))


    if slime.get() == False:
        get = False
        list_f[col].change()
        slime.iss = None


    pygame.display.flip()
    

pygame.quit()
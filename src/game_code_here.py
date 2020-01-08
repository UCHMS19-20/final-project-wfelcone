import pygame
import sys
pygame.font.init()

pygame.init()

screen = pygame.display.set_mode( (1000, 400) )

classic_blue = (15, 76, 129)

myfont=pygame.font.SysFont('Comic Sans MS', 50)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    pygame.time.delay(100)
    screen.fill(classic_blue)
    textsurface = myfont.render("FORTNITE 2", False, (255, 255, 255))
    screen.blit(textsurface, (350, 10))
    pygame.display.flip()

    pygame.draw.rect(screen,(255,0,255),(20,20, 20,20))
    pygame.display.flip()
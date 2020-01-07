import pygame
import sys

pygame.init()

screen = pygame.display.set_mode( (1000, 400) )

classic_blue = (15, 76, 129)

myfont=pygame.font.SysFont('Comic Sans MS', 12)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    pygame.time.delay(100)
    screen.fill(classic_blue)
    pygame.display.flip()

    #textsurface = myfont.render("We Live in a Soceity"), False, (0, 0, 0))
    #win.blit(textsurface, (10, 10))
    #pygame.display.flip()


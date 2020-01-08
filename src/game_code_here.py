import pygame
import sys
pygame.font.init()

pygame.init()

screen = pygame.display.set_mode( (1000, 400) )

classic_blue = (15, 76, 129)

myfont=pygame.font.SysFont('Arial', 12)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    pygame.time.delay(100)
    screen.fill(classic_blue)
    textsurface = myfont.render("Sample Text", False, (0, 0, 0))
    screen.blit(textsurface, (10, 10))
    pygame.display.flip()


import pygame
import sys
pygame.font.init()

pygame.init()

screen = pygame.display.set_mode( (1000, 500) )

#There are the RGB values for all the colors in the game
classic_blue = (15, 76, 129)
tangerine_tango = (221, 65, 36)
greenery = (136, 176, 75)
serenity = (176, 205, 223)

myfont=pygame.font.SysFont('Comic Sans MS', 50)

player = {
    "width": 20,
    "height": 50,
    "x": 250,
    "y": 250,
    "velocity": 20
}

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player["x"] -= player["velocity"]

    if keys[pygame.K_RIGHT]:
        player["x"] += player["velocity"]

    if keys[pygame.K_UP]:
        player["y"] -= player["velocity"]
        
    if keys[pygame.K_DOWN]:
        player["y"] += player["velocity"]

    pygame.draw.rect(screen, (tangerine_tango), (player["x"], player["y"], player["width"], player["height"]))
    pygame.display.update()

    pygame.time.delay(100)
    screen.fill(serenity)
    textsurface = myfont.render("FORTNITE 2", False, (classic_blue))
    screen.blit(textsurface, (350, 10))
    pygame.display.flip()

    #pygame.draw.rect(screen,(255,0,255),(20,20, 20,20))
    #pygame.display.flip()
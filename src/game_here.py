import pygame
import sys


#pygame.font.init()
#myfont = pygame.font.SysFont("monospace", 50)
 
# -- Global constants
 
# Colors
classic_blue = (15, 76, 129)
tangerine_tango = (221, 65, 36)
greenery = (136, 176, 75)
serenity = (176, 205, 223)
mimosa = (240, 192, 90)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
 
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
pygame.display.set_caption('Maize Maze by Kojima Productions')
 
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.Surface([15, 15])
        self.image.fill(tangerine_tango)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(greenery)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

#---Exterior walls------------------------------------------

#Left exterior wall
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

#Top exterior wall
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
#Right exterior wall
wall = Wall(790, 0, 10, 450)
wall_list.add(wall)
all_sprite_list.add(wall)

#Bottom exterior wall
wall = Wall(10, 440, 780, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#---Spawn walls------------------------------------------

#Spawn wall bottom
wall = Wall(10, 60, 20, 440)
wall_list.add(wall)
all_sprite_list.add(wall)

#Spawn wall right
wall = Wall(100, 30, 200, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 30, 10, 30)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(30, 420, 200, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 390, 400, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 60, 10, 330)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(80, 60, 30, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(330, 10, 220, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(80, 60, 30, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 180, 130, 10)
wall_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(250, 400, 200, 20)
wall_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(130, 130, 50, 50)
wall_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(130, 60, 50, 50)
wall_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(200, 60, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)


wall = Wall(200, 60, 130, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(330, 50, 200, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(520, 90, 30, 80)
wall_list.add(wall)
all_sprite_list.add(wall)
#---Letters-----------------------------------------------
#The letter that it is is captialized

#maize
#mazE

wall = Wall(740, 20, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(740, 20, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(740, 70, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(740, 45, 30, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#maizE
#maze

wall = Wall(740, 90, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(740, 90, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(740, 140, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(740, 115, 30, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#maiZe
#maze

wall = Wall(690, 20, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(690, 70, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(700, 50, 10, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(710, 30, 10, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

#maize
#maZe

wall = Wall(690, 90, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(690, 140, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(700, 120, 10, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(710, 100, 10, 20)
wall_list.add(wall)
all_sprite_list.add(wall)

#maIze 
#maze

wall = Wall(670, 20, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

#mAize
#maze

wall = Wall(650, 20, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(620, 20, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(620, 20, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(620, 40, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#maize 
#mAze

wall = Wall(670, 90, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(640, 90, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(640, 90, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(640, 110, 40, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#Maize 
#maze

wall = Wall(600, 20, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(570, 20, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(580, 30, 20, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#maize
#Maze

wall = Wall(620, 90, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(590, 90, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(600, 100, 20, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#---Text border walls---------------------------------

wall = Wall(550, 10, 10, 160)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(550, 160, 240, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#---Stuff---------------------------------------------

player = Player(25, 25)
player.walls = wall_list
 
all_sprite_list.add(player)
 
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
    all_sprite_list.update()

    
 
    screen.fill(mimosa)
 
    #textsurface = myfont.render("FORTNITE 2", False, (classic_blue))
    #screen.blit(textsurface, (350, 10))
    #pygame.display.flip()
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
import pygame
import sys

 
# -- Global constants
 
# Colors
classic_blue = (15, 76, 129)
tangerine_tango = (221, 65, 36)
greenery = (136, 176, 75)
serenity = (176, 205, 223)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Fortnite 2')
 
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(tangerine_tango)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(greenery)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
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
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#Spawn wall right
wall = Wall(100, 100, 10, 100)
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


# Create the player paddle object
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
 

    screen.fill(serenity)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
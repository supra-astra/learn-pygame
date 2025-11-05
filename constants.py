import pygame 

# width and height of our game window
width = 800 
height = 400

#set the title of window
pygame.display.set_caption('Basic Game')

#clock helps us with time and framerate
clock = pygame.time.Clock()


# surface made with color
surface_w = 100
surface_h = 200
test_surface = pygame.Surface((surface_w,surface_h))
# add color to it
test_surface.fill('Red')

sky_surface = pygame.image.load("assets/sky.png")
ground_surface = pygame.image.load("assets/ground.png")

snail_surface = pygame.image.load("assets/snail/snail1.png")
player_surface = pygame.image.load("assets/player/player_walk_1.png")

# left,top,width,height 
#player_rect = pygame.Rect()
# get rectangle the same size as it
# midleft, midbottom, topleft, topright ....
player_rect = player_surface.get_rect(topleft = (80,210))

snail_x_pos = 600
snail_y_pos = 250

player_x_pos = 800
player_y_pos = 250

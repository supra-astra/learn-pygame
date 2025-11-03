import pygame
from sys import exit


# width and height of our game window
width = 800 
height = 400

#set the title of window
pygame.display.set_caption('Runner')

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


def main():
    # instantiesaties pygame , play sounds and images
    # and other complicated stuff
    pygame.init()

    # display the surface -> the window that the players are
    # gonna see
    screen = pygame.display.set_mode((width,height))

    # main game loop that runs forever
    while True:
        #event loop
        # look at all possible player input and check
        for event in pygame.event.get():
            # pygame.event.get() will get us all the events
            if event.type == pygame.QUIT:
                # like the x button of windows to close
                pygame.quit()
                #close pygame
                exit()

        #display the surface
        # blit is a block image transform -> put another surface
        # on another.
        # 2nd arg is posn we place it
        # (left,top) 
        #screen.blit(test_surface,(200,100))        
        # instead of the offset , keep it in the frame
        screen.blit(ground_surface, (0,0))
        screen.blit(sky_surface,(200,100))
                
        # draw all our elements and update everything
        # updates the screen display surface
        pygame.display.update()
        # while True loop shouldnt run faster than 60ms
        clock.tick(60)
        
        


if __name__ == "__main__":
    main()

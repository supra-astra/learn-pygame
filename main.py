import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "Github Gameoff 2025"

import pygame
from sys import exit
from constants import *



def main():
    # instantiesaties pygame , play sounds and images
    # and other complicated stuff
    pygame.init()


    # font
    test_font = pygame.font.Font("assets/Pixeltype.ttf",50)

    # text info
    text_surface = test_font.render("My game",False,"Red")
    
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
        # and the order matters
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        # surface with some text
        # creating text
        ## create a font(text size and style)
        ## write text on a surface
        ## blit the text surface
        screen.blit(text_surface,(300,50))
        # create an image of the text
        # place it on the display surface
        global snail_x_pos
        snail_x_pos -= 4
        if snail_x_pos < 100:
            snail_x_pos = 800

        global player_x_pos
        player_x_pos -= 6
        if player_x_pos < 100:
            player_x_pos = 800

        global snail_suface
        snail_surface.convert_alpha()

        global player_surface 
        player_surface.convert_alpha()
        screen.blit(snail_surface,(snail_x_pos,snail_y_pos))
        #screen.blit(player_surface,(player_x_pos,player_y_pos))
        screen.blit(player_surface,player_rect)

                       
        # draw all our elements and update everything
        # updates the screen display surface
        pygame.display.update()
        # while True loop shouldnt run faster than 60ms
        clock.tick(60)
        
                


if __name__ == "__main__":
    main()

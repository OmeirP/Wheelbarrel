# Shop Module. not working inside main file to keep clean.
import pygame
import WheelBarrELGame
from WheelBarrELGame import *

shopScreen = False


def shop(): # trigger shop func through button added on menu in game_intro
    shopScreen = True
    while shopScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(menuBackgroundImg, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 88)
        TextSurf, TextRect = set_colour("Shop", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go!",150,450,100,50,green,bright_green,"play") #Change go to return to menu and change play to string to go to game_intro func
        button("Exit",550,450,100,50,red,bright_red,"quit") # keep same

        mouse = pygame.mouse.get_pos()

        """if 550+100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, red, (550,450,100,50))"""



        pygame.display.update()
        clock.tick(15)

# Shop Module. not working inside main file to keep clean.
import pygame
import WheelBarrELGame
#from WheelBarrELGame import *

shopScreen = False


def market(): # trigger shop func through button added on menu in game_intro
    shopScreen = True
    while shopScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        WheelBarrELGame.gameDisplay.blit(WheelBarrELGame.menuBackgroundImg, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 88)
        TextSurf, TextRect = WheelBarrELGame.set_colour("Shop", largeText)
        TextRect.center = ((WheelBarrELGame.display_width/2), (WheelBarrELGame.display_height/2))
        WheelBarrELGame.gameDisplay.blit(TextSurf, TextRect)

        #WheelBarrELGame.button("Back",150,450,100,50,WheelBarrELGame.green,WheelBarrELGame.bright_green,"mainMenu") #Change go to return to menu and change play to string to go to game_intro func
        WheelBarrELGame.button("Exit",650,500,100,50,WheelBarrELGame.red,WheelBarrELGame.bright_red,"quit") # keep same

        mouse = pygame.mouse.get_pos()

        """if 550+100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, red, (550,450,100,50))"""



        pygame.display.update()
        WheelBarrELGame.clock.tick(15)

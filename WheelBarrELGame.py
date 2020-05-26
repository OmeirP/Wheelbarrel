import pygame
import time
import random
import _thread
import shelve
import shopUpgrades

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)#test sdijdf
white = (255,255,255) # 256 choices, including 0
red = (200,0,0) # red first
green = (0,200,0)
blue = (0,0,200)
bright_blue = (0,0,255)
orange = (255,165,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


obs_colour = (69,42,162)

wheel_barrel_width = 245/4
wheel_barrel_height = 378/4

crashScreen = False
pause = False


gameDisplay = pygame.display.set_mode((display_width,display_height))  #resolution size. 2 pairs of brackets because otherwise python sees two args instead of a tuple.
pygame.display.set_caption('WheelbarrelGame')
clock = pygame.time.Clock()

wheelBarrelImg = pygame.image.load('WheelBarrEL.png')
wheelBarrelImg = pygame.transform.scale(wheelBarrelImg, ((245//4),(378//4)))

wbIcon = pygame.image.load('WheelBarrEL.png')
pygame.display.set_icon(wbIcon)

backgroundImg = pygame.image.load('backgroundpng.png')

menuBackgroundImg = pygame.image.load('menuBackground.png')

obstImage = pygame.image.load('obstImagewsspng.png')

secmenbg=pygame.image.load('secondarymenubg.png')

#winImg = pygame.draw.rect(gameDisplay,black,(random.randrange(0, display_width),0, 2, 2) ))

#highscore = 0 #read contents of txt file to this var

hsvpath="J:/Dev/Wheelbarrel/HSV.txt"

hsvfile= open(hsvpath,'r+') #close in gameExit function

highscore = hsvfile.read()



"""highscore = shelve.open("highscorevalue.txt")

highscore['highscorething']"""


#def scoreupdate(dodged, score):
#    while True:
#        score = dodged



#def things_dodged(dcount, score):
#    font = pygame.font.SysFont(None, 25)
#    text = font.render("Obstacles dodged: " + str(dcount) + "/nScore: " + str(score) + "/nHighscore: " + highScore, True, black)
#    gameDisplay.blit(text, (0,0))


#def air():
#    gameDisplay.blit(winImg, (random.randrange(0, display_width),(random.randrange(0, display_width), 2, 2) ))


def highscorereblit(dodged):
    global highscore

    if dodged > int(highscore):
        highscore = dodged
        hsvfile= open(hsvpath,'r+')
        hsvfile.write(str(dodged))
        

    font = pygame.font.SysFont(None, 25)
    text2 = font.render("Highscore: " + str(highscore), True, black)
    gameDisplay.blit(text2, (0,25))




def things_dodged(dcount):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(dcount), True, black)
    gameDisplay.blit(text, (0,0))



def things(thingx, thingy, thingw, thingh, colour):
    gameDisplay.blit(obstImage, (thingx, thingy))



def wheelbarrel(x,y):
    gameDisplay.blit(wheelBarrelImg, (x,y))


def set_colour(text, font):
    if crashScreen == True:
        textSurface = font.render(text, True, green)     #IMPORTANT True is for antialiasing.
        return textSurface, textSurface.get_rect()
    elif pause == True:
        textSurface = font.render(text, True, green)
        return textSurface, textSurface.get_rect()
    else:
        textSurface = font.render(text, True, black)     #IMPORTANT True is for antialiasing.
        return textSurface, textSurface.get_rect()


def text_object(text, font):
    set_colour(text, font)





def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 88)
    TextSurf, TextRect = set_colour(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()





def button(msg,x,y,w,h,ic,ac,action=None):
      #button time

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "unpause":
                unpause()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = set_colour(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def crash():
    global crashScreen
    crashScreen = True

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(secmenbg, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 88)
        TextSurf, TextRect = set_colour("U cRasH?!", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Retry",150,450,100,50,blue,bright_blue,"play")
        button("Exit",550,450,100,50,red,bright_red,"quit")


        mouse = pygame.mouse.get_pos()


        pygame.display.update()
        clock.tick(15)



def unpause():
    global pause
    pause = False


def paused():
    gameDisplay.blit(secmenbg, (0,0))
    largeText = pygame.font.Font('freesansbold.ttf', 88)
    TextSurf, TextRect = set_colour("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",150,450,100,50,blue,bright_blue,"unpause")
        button("Exit",550,450,100,50,red,bright_red,"quit")


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
                if event.key == pygame.K_SPACE:
                    unpause()

        mouse = pygame.mouse.get_pos()


        pygame.display.update()
        clock.tick(15)



#Put altered game_intro func for shop and trigger with button inside game_intro function.
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(menuBackgroundImg, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 88)
        TextSurf, TextRect = set_colour("Wheelbarrel", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go!",150,450,100,50,green,bright_green,"play")
        button("Exit",550,450,100,50,red,bright_red,"quit")

        mouse = pygame.mouse.get_pos()

        """if 550+100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, red, (550,450,100,50))"""



        pygame.display.update()
        clock.tick(15)



def game_loop():
    global pause


    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 90
    thing_height = 90

#    thingCount = 1



    dodged = 0


    # while True:

#    if score >= highscore:
#        highscore = score

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        #gameDisplay.fill(green) # whole display filled, to not paint over car, put first.

        gameDisplay.blit(backgroundImg, (0, 0))

#        scoreupdate(dodged, score)

        #things(thingx, thingy, thingw, thingh, colour)
        things(thing_startx, thing_starty, thing_width, thing_height, obs_colour)
        thing_starty += thing_speed
        wheelbarrel(x,y)
        things_dodged(dodged)
        highscorereblit(dodged)


        if x > display_width - wheel_barrel_width or x < 0: #x is top right corner of barrel
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if dodged % 3 == 0:
                thing_speed *= 1.3

        if y < thing_starty+thing_height:
            #print("y crossover")
            pass

            if x > thing_startx and x < thing_startx + thing_width or x + wheel_barrel_width > thing_startx and x + wheel_barrel_width < thing_startx + thing_width:
                if y > thing_starty and y < thing_starty + thing_height or y + wheel_barrel_height > thing_starty and y + wheel_barrel_height < thing_starty + thing_height:
                    crash()



        pygame.display.update()
        clock.tick(60)  #tick is for fps

#def scoreupdate(dodged):
#    while True:
#        score = dodged

#_thread.start_new_thread(scoreupdate)

game_intro()
game_loop()
pygame.quit()
quit()

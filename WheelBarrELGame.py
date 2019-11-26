import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)#test
white = (255,255,255) # 256 choices, including 0
red = (255,0,0) # red first
green = (0,255,0)

obs_colour = (69,42,162)

wheel_barrel_width = 270/4


gameDisplay = pygame.display.set_mode((display_width,display_height))  #resolution size. 2 pairs of brackets because otherwise python sees two args instead of a tuple.
pygame.display.set_caption('Get ur driving license')
clock = pygame.time.Clock()

wheelBarrelImg = pygame.image.load('WheelBarrEL.png')
wheelBarrelImg = pygame.transform.scale(wheelBarrelImg, ((245//4),(378//4)))

backgroundImg = pygame.image.load('backgroundpng.png')


def things_dodged(dcount):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Obstacles dodged: " + str(dcount), True, black)
    gameDisplay.blit(text, (0,0))




def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingw, thingh])



def wheelbarrel(x,y):
    gameDisplay.blit(wheelBarrelImg, (x,y))

def text_object(text, font):
    textSurface = font.render(text, True, black)     #IMPORTANT True is for antialiasing.
    return textSurface, textSurface.get_rect()





def messgae_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 88)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()


def crash():
    messgae_display("You done crashed")


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        #gameDisplay.fill(green) # whole display filled, to not paint over car, put first.

        gameDisplay.blit(backgroundImg, (0, 0))

        #things(thingx, thingy, thingw, thingh, colour)
        things(thing_startx, thing_starty, thing_width, thing_height, obs_colour)
        thing_starty += thing_speed
        wheelbarrel(x,y)
        things_dodged(dodged)

        if x > display_width - wheel_barrel_width or x < 0:#x is top right corner of barrel
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if dodged % 3 == 0:
                thing_speed *= 1.3

        if y < thing_starty+thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x + wheel_barrel_width > thing_startx and x + wheel_barrel_width < thing_startx + thing_width:
                print("x crossover")
                crash()



        pygame.display.update()
        clock.tick(60)  #tick is for fps


game_loop()
pygame.quit()
quit()
import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255) # 256 choices, including 0
red = (255,0,0) # red first
green = (0,255,0)

wheel_barrel_width = 128


gameDisplay = pygame.display.set_mode((display_width,display_height))  #resolution size. 2 pairs of brackets because otherwise python sees two args instead of a tuple.
pygame.display.set_caption('Racey but not really')
clock = pygame.time.Clock()

wheelBarrelImg = pygame.image.load('WheelBarrEL.png')
wheelBarrelImg = pygame.transform.scale(wheelBarrelImg, (221,128))



def wheelbarrel(x,y):
    gameDisplay.blit(wheelBarrelImg, (x,y))


def game_loop():

    x = (display_width * 0.4)
    y = (display_height * 0.75)

    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(green) # whole display filled, to not paint over car, put first.
        wheelbarrel(x,y)

        if x > display_width - wheel_barrel_width or x < 0:#x is top right corner of barrel
            gameExit = True

        pygame.display.update()
        clock.tick(60)  #tick is for fps


game_loop()
pygame.quit()
quit()
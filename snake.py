import pygame as pg
import time
import random

pg.init()

# surface
gd = pg.display

width = 800
height = 600

screen = gd.set_mode((width, height))
gd.set_caption("PySnake")
clock = pg.time.Clock()

blockSize = 20

font = pg.font.SysFont(None, 30)
#img = pg.image.load('image.ext')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

snakeList = [(200, 200), (190, 200), (180, 200)]

screen.fill(white)


def clearScreen():
    screen.fill(white)
    gd.update()


def drawSnake():
    for x, y in snakeList:
        pg.draw.rect(screen, green, [x, y, blockSize, blockSize])


def moveSnake(x, y):
    prev = (x, y)
    for x in range(len(snakeList)):
        prev, snakeList[x] = snakeList[x], prev


def snakeColide():
    return snakeList[0] in snakeList[1:]


def messageToScreen(msg, color, x=(width-100)/2, y=(height-25)/2, centered = False):
    # Message, antialising, color
    txt = font.render(msg, True, color)
    if centered:
    	rect = txt.get_rect()
    	rect.center = (width/2), (height/2)
    	screen.blit(txt, rect)
    else:
    	screen.blit(txt, [x, y])
    gd.update()


def genFood():
        x = random.randrange(0, width-blockSize, blockSize)
        y = random.randrange(0, height-blockSize, blockSize)

        while (x, y) in snakeList:
            x = random.randrange(0, width-blockSize, blockSize)
            y = random.randrange(0, height-blockSize, blockSize)

        return (x, y)


def gameOverMessage():
    messageToScreen("Game Over!", red, centered = True)
    time.sleep(3)


def gameLoop():
    fps = 10

    leadX = snakeList[0][0]
    leadY = snakeList[0][1]

    foodX, foodY = genFood()

    # direction = up - 1, down - 2, left - 3, right - 4
    direction = 4

    running = True
    gameOver = False
    pause = False
    turbo = False

    while running:

        if gameOver:
            clearScreen()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                    running = False

                if event.key == pg.K_p:
                    pause = not pause
                if event.key == pg.K_SPACE:
                	turbo = True

                # Eixo Y
                if event.key == pg.K_DOWN and direction != 1:
                    direction = 2
                elif event.key == pg.K_UP and direction != 2:
                    direction = 1
                # Eixo X
                elif event.key == pg.K_RIGHT and direction != 3:
                    direction = 4
                elif event.key == pg.K_LEFT and direction != 4:
                    direction = 3

            elif event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                	turbo = False

        if pause:
        	continue

        if direction == 1:
            leadY -= blockSize
        elif direction == 2:
            leadY += blockSize
        elif direction == 3:
            leadX -= blockSize
        elif direction == 4:
            leadX += blockSize

        moveSnake(leadX, leadY)

        # checking if the snake hit the main walls, going out of screen, or hit itself
        if leadX < 0 or leadX > width or leadY < 0 or leadY > height or snakeColide():
            gameOverMessage()
            gameOver = True

        screen.fill(white)

        # draw thew apple/food
        # screen.fill(red, [200,200,10,10])
        pg.draw.rect(screen, red, [foodX, foodY, blockSize, blockSize])

        # draw the snake
        drawSnake()

        gd.update()

        if leadX == foodX and leadY == foodY:
            snakeList.append(snakeList[-1])
            if len(snakeList)%10 == 0:
            	fps += 5
            	fps = min(fps,60)

            foodX, foodY = genFood()

        speed = fps
        if turbo:
        	speed = 60
        clock.tick(speed)

        while gameOver:
            messageToScreen("Press Q to Quit or C to Continue playing.", red, centered = True)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                        running = False
                        gameOver = False
                        leadX, leadY = 200, 200
                    elif event.key == pg.K_c:
                        leadX, leadY = 200, 200
                        gameOver = False

    pg.quit()
    quit()

gameLoop()

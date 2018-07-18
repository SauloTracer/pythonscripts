import pygame as pg
import time
import random

pg.init()

# surface
gd = pg.display

width = 800
height = 600
blockSize = 20
fps = 10
# direction = up - 1, down - 2, left - 3, right - 4
direction = 4

screen = gd.set_mode((width, height))
gd.set_caption("PySnake")
clock = pg.time.Clock()

font = pg.font.SysFont(None, 30)

imgHead = pg.image.load('head.png')
imgTail = pg.image.load('tail.png')
body = pg.image.load('body.png')
apple = pg.image.load('apple.png')

head = imgHead
tail = pg.transform.rotate(imgTail, -90)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (14,209,69) #(0, 255, 0)
blue = (0, 0, 255)

snakeList = []

screen.fill(white)


def clearScreen():
    screen.fill(white)
    gd.update()


def drawSnake():
    screen.blit(head, snakeList[0])

    for pos in snakeList[1:-1]:
        #pg.draw.rect(screen, green, [x, y, blockSize, blockSize])
        screen.blit(body, pos)

    if snakeList[-1][0] < snakeList[-2][0]:
        tail = pg.transform.rotate(imgTail, -90)
    elif snakeList[-1][0] > snakeList[-2][0]:
        tail = pg.transform.rotate(imgTail, 90)
    elif snakeList[-1][1] > snakeList[-2][1]:
        tail = imgTail
    else:
    	tail = pg.transform.rotate(imgTail, 180)
    screen.blit(tail,snakeList[-1])

def moveSnake(direction):
    global head

    x,y = snakeList[0]

    if direction == 1: #up
        y -= blockSize
        head = imgHead
    elif direction == 2: #down
        y += blockSize
        head = pg.transform.rotate(imgHead,180)
    elif direction == 3: #left
        x -= blockSize
        head = pg.transform.rotate(imgHead, 90)
    elif direction == 4: #right
        x += blockSize
        head = pg.transform.rotate(imgHead, -90)

    prev = (x, y)
    for x in range(len(snakeList)):
        prev, snakeList[x] = snakeList[x], prev


def snakeColide():
	x,y = snakeList[0]
	# checking if the snake hit any wall, went out of screen, or hit itself
	return x < 0 or x > width or y < 0 or y > height or snakeList[0] in snakeList[1:]


def messageToScreen(msg, color, x=(width-100)/2, y=(height-25)/2, centered = False, displaceX = 0, displaceY = 0):
    # Message, antialising, color
    txt = font.render(msg, True, color)
    if centered:
    	rect = txt.get_rect()
    	rect.center = (width/2)+displaceX, (height/2)+displaceY
    	screen.blit(txt, rect)
    else:
    	screen.blit(txt, [x+displaceX, y+displaceY])
    gd.update()


def genFood():
        x = random.randrange(0, width-blockSize, blockSize)
        y = random.randrange(0, height-blockSize, blockSize)

        while (x, y) in snakeList:
            x = random.randrange(0, width-blockSize, blockSize)
            y = random.randrange(0, height-blockSize, blockSize)

        return (x, y)


def gameOverMessage():
    messageToScreen("Game Over!", red, centered = True, displaceY = -25)
    messageToScreen("Press C to Continue playing or Q to Quit.", black, centered = True, displaceY = 25)

def checkFood():
    global food
    global fps

    x, y = snakeList[0]
    if snakeList[0] == food:
        snakeList.append(snakeList[-1])
        if len(snakeList)%10 == 0:
            fps = min(fps + 2, 60)
        food = genFood()


def reset():
    global food
    global snakeList
    global fps
    global direction

    food = genFood()
    snakeList = [(200, 200), (190, 200), (180, 200)]
    fps = 10
    direction = 4

def gameLoop():
    global direction

    running = True
    gameOver = False
    pause = False
    turbo = False

    while running:

        while gameOver:
            gameOverMessage()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                        running = False
                        gameOver = False
                        reset()
                    elif event.key == pg.K_c:
                        reset()
                        gameOver = False
        
        if not running:
            continue

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

        moveSnake(direction)
        if snakeColide():
            gameOver = True
            turbo = False

        if not gameOver:
        	screen.fill(white)

	        # draw the apple/food
	        #pg.draw.rect(screen, red, [food[0], food[1], blockSize, blockSize])
	        screen.blit(apple, food)

	        # draw the snake
	        drawSnake()
	        checkFood()
	        gd.update()

        speed = fps
        if turbo:
        	speed = 60
        clock.tick(speed)

    pg.quit()
    quit()

reset()
gameLoop()

import pygame
import random
from collections import namedtuple

Color = namedtuple("Color", ['white', 'orange', 'green', 'blue', 'yellow'])

Color.white = (255,255,255)
Color.orange = (255,201,14)
Color.green = (0,156,59)
Color.yellow = (255,223,0)
Color.blue = (0,39,118)

def drawFlag(canvas):
	# 20 x 14
	pygame.draw.rect(canvas, Color.green, pygame.Rect(50, 80, 200,140))
	
	# 1,7 de distância da borda nos 4 vértices do losângulo
	pygame.draw.polygon(canvas, Color.yellow, [(67,150), (150,97), (233,150), (150,203)])

	# raio de 3,6
	pygame.draw.circle(canvas, Color.blue, [150,150], 36)

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

def growing_squares(canvas):
	pos, size = 0, 10
	for x in range(6):
		pygame.draw.rect(canvas, random_color(), [pos, pos, size, size])
		pos += size
		size = size*2

def main():
	pygame.init()
	canvas = pygame.display.set_mode([300,300])
	pygame.display.set_caption("Pygame testing")

	clock = pygame.time.Clock()

	canvas.fill(Color.orange)
	panels = [
		(pygame.Surface((5,5)), [0,0]), 
		(pygame.Surface((5,5)), [295,295]), 
		(pygame.Surface((5,5)), [295,0]), 
		(pygame.Surface((5,5)), [0,295])
	]
	rect = pygame.Rect(110,110,45,45)

	growing_squares(canvas)

	running = True
	while running:
	
		#Listen and process events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
					break
			if event.type == pygame.MOUSEBUTTONDOWN:
				growing_squares(canvas)
				#rect.move(10,10)
			if event.type == pygame.MOUSEMOTION:
				canvas.fill(random_color())
				drawFlag(canvas)

		clock.tick(30)

		#process panels and surfaces and stuff
		for x,p in panels:
			canvas.blit(x,p)

		#update screen
		pygame.display.update()

	#close the window
	pygame.quit()

main()
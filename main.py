# http://www.coderholic.com/boids/
import random, math
import pygame, sys
from pygame.locals import *
from entrega import *

SIZE 				= WIDTH, HEIGHT	= 800, 600
MAX_SPEED			= 10
GOLDFISH, OCEANBLUE	= Color(243, 134, 48), Color(28, 107, 160)
MAX_DISTANCE		= 100
N					= 4

pygame.init()
screen = pygame.display.set_mode(SIZE)
boids = generarCardumen(N, WIDTH, HEIGHT, 10)
while True:
	screen.fill(OCEANBLUE)
	for i in range(len(boids)):
		close		= vecindad(i, boids, MAX_DISTANCE)
		boids[i]	= moveCloser(boids[i], close) # COHESION
		boids[i]	= moveWith(boids[i], close) # ALINEAMIENTO
		boids[i]	= moveAway(boids[i], close, 20) # SEPARATION

		boids[i] = corregir(boids[i], WIDTH, HEIGHT)
		boids[i] = move(boids[i], MAX_SPEED) # MOVER
		try:
			pygame.draw.circle(screen, GOLDFISH, [int(boids[i][0][0]), int(boids[i][0][1])], 3, 0)
		except:
			print(boids[i])
	pygame.display.flip()
	pygame.time.delay(29)

	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): # Se cierra el programa
			pygame.quit()
			sys.exit()

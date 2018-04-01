import pygame

COLORS = {
			'black' : (0, 0, 0),
			'white' : (255,255,255),
			'red' : (255, 0, 0),
			'green' : (0, 255, 0),
			'blue' : (255, 0, 0)
		}

TOP = 10
EDGES = 15
ORIGIN = (0, 0)
PADDING = 15
INCREMENT = 5
SHARK_INCREMENT = 1
PLAYER_LINE_WIDTH = 10

SIZE = WIDTH, HEIGHT = 640, 480

DIRECTIONS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
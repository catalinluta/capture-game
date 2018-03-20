import sys, pygame
import utils

TOP = 10
EDGES = 15

pygame.init()

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
	def drawOnDisplay(self,display):
		display.blit(self.image, self.rect)
	def scale(self,dimension):
		self.image = pygame.transform.scale(self.image,dimension)
		self.rect = self.image.get_rect()


active_background = Background("background.jpg",[0,0])
gray_background = Background("background_gray.jpg",[0,0])

size = width, height = 1280, 960
speed = [1, 1]

screen = pygame.display.set_mode(size)

#TODO : Create constants for percentages
game_area_width = int(round(width * 0.8))
game_area_height = int(round(height * 0.8))

game_area_start_width = int(round(width * 0.1))
game_area_start_height = int(round(height * 0.05))

#TODO : Create constant for Game Area Dimension
game_area = pygame.Surface((game_area_width,game_area_height))
game_area_rect = game_area.get_rect()

active_background.scale((game_area_width,game_area_height))
gray_background.scale((game_area_width,game_area_height))

ball = pygame.image.load("bug1.png")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	gray_background.drawOnDisplay(game_area)
	active_background.drawOnDisplay(game_area)
	game_area.blit(ball, ballrect)
	screen.blit(game_area,(game_area_start_width,game_area_start_height))
	pygame.display.flip()
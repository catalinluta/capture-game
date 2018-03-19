import sys, pygame
import utils

pygame.init()

class Background(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location
	def drawOnDisplay(self,display):
		display.blit(self.image, self.rect)


background = Background("background.jpg",[0,0])

size = width, height = 1280, 960
speed = [1, 1]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("bug1.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    background.drawOnDisplay(screen)
    screen.blit(ball, ballrect)
    pygame.display.flip()
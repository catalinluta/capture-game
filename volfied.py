import sys, pygame
import utils
from game_area import GameArea
from background import Background
from boat import Boat
from shark import Shark
from collections import deque
import os

# TODO 1: randomly generate creep position
# TODO 2 : must create an available area for creeps to move in

'''
This should be moved in the boat class. Need to refactor such that all variables are available
'''

clock = pygame.time.Clock()

pygame.init()

game_area = GameArea(int(round(utils.WIDTH * 0.8)), int(round(utils.HEIGHT * 0.8)))

game_area_start = game_area_start_width, game_area_start_height = (int(round(utils.WIDTH * 0.1)), int(round(utils.HEIGHT * 0.05)))

active_background = Background("assets"+os.sep+"water.jpg", utils.ORIGIN)
gray_background = Background("assets"+os.sep+"water_gy.jpg", utils.ORIGIN)

screen = pygame.display.set_mode(utils.SIZE)

active_background.scale(game_area.getDim())
gray_background.scale(game_area.getDim())

shark = Shark("assets"+os.sep+"shark-fin.png", game_area.getRect().bottomright[0]/2, game_area.getRect().bottomright[1]/2-utils.PLAYER_LINE_WIDTH, pygame.K_RIGHT, game_area.getDim())

boat = Boat("assets"+os.sep+"ship.png", game_area.getRect().bottomright[0]/2, game_area.getRect().bottomright[1], pygame.K_RIGHT)

direction_list = deque([])

dead = False

while not dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in utils.DIRECTIONS:
                if event.key not in direction_list:
                    direction_list.append(event.key)
            elif event.key == pygame.K_SPACE:
                boat.startCapturing()
        if event.type == pygame.KEYUP:
            if event.key in utils.DIRECTIONS:
                if event.key in direction_list:
                    direction_list.remove(event.key)
    if len(direction_list) != 0:
        boat.move(direction_list[0],game_area)

    shark.move(game_area)

    screen.fill(utils.COLORS['white'])
    gray_background.drawOnDisplay(game_area)
    active_background.drawOnDisplay(game_area)
    game_area.blit(shark.getSurface(), shark.getPos())
    if boat.capture and len(boat.capturing) > 1:
        pygame.draw.lines(game_area.getSurface(), utils.COLORS['green'],False, boat.capturing, utils.PADDING)
    pygame.draw.polygon(game_area.getSurface(), utils.COLORS['green'], game_area.getPlayerCircuit(), utils.PADDING)
    game_area.blit(boat.getSurface(), boat.getDrawPos())
    screen.blit(game_area.getSurface(), game_area_start)
    pygame.display.flip()
    clock.tick(60)
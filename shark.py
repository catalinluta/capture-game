__author__ = 'luta'
import pygame
import random
import utils
from collections import deque

class Shark:
    surface = None
    rect = None
    x = None
    y = None
    direction = None
    poi = deque([])
    current_poi= None

    def __init__(self, image, x, y, direction, active_area):
        self.x = x
        self.y = y
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect()
        self.direction = direction

        for i in range(3):
            self.generatePoi(active_area)
        self.current_poi = self.poi.popleft()

    def generatePoi(self,active_area):
        valid = False

        goal_x = random.choice(range(active_area[0]))
        goal_y = random.choice(range(active_area[1]))

        while not valid:
            if goal_x >= utils.PLAYER_LINE_WIDTH and goal_x <= active_area[0] - utils.PLAYER_LINE_WIDTH:
                if goal_y >= utils.PLAYER_LINE_WIDTH and goal_y <= active_area[1] - utils.PLAYER_LINE_WIDTH:
                    valid = True
                else:
                    goal_y = round(int(float(random.choice(range(int(self.getY())))) * 2))
            else:
                goal_x = round(int(float(random.choice(range(int(self.getX())))) * 2))

        self.poi.append((goal_x, goal_y))

    def getPos(self):
        return (self.x, self.y)

    def getX(self):
        return self.x

    def moveX(self, direction, increment):
        if direction == pygame.K_RIGHT:
            self.x += increment
        elif direction == pygame.K_LEFT:
            self.x -= increment
        if self.direction != direction:

            if self.direction == pygame.K_UP and direction == pygame.K_RIGHT:
                self.surface = pygame.transform.rotate(self.surface, -90)
            elif self.direction == pygame.K_UP and direction == pygame.K_LEFT:
                self.surface = pygame.transform.rotate(self.surface, 90)
            elif self.direction == pygame.K_DOWN and direction == pygame.K_RIGHT:
                self.surface = pygame.transform.rotate(self.surface, 90)
            elif self.direction == pygame.K_DOWN and direction == pygame.K_LEFT:
                self.surface = pygame.transform.rotate(self.surface, -90)
            else:
                self.surface = pygame.transform.flip(self.surface, True, False)
            self.direction = direction

    def getY(self):
        return self.y

    def moveY(self, direction, increment):
        if direction == pygame.K_UP:
            self.y -= increment
        elif direction == pygame.K_DOWN:
            self.y += increment
        if self.direction != direction:
            if self.direction == pygame.K_LEFT and direction == pygame.K_UP:
                self.surface = pygame.transform.rotate(self.surface, -90)
            elif self.direction == pygame.K_LEFT and direction == pygame.K_DOWN:
                self.surface = pygame.transform.rotate(self.surface, 90)
            elif self.direction == pygame.K_RIGHT and direction == pygame.K_UP:
                self.surface = pygame.transform.rotate(self.surface, 90)
            elif self.direction == pygame.K_RIGHT and direction == pygame.K_DOWN:
                self.surface = pygame.transform.rotate(self.surface, -90)
            else:
                self.surface = pygame.transform.flip(self.surface, False, True)
            self.direction = direction

    def validatePosition(self,direction, game_area):
        if direction == pygame.K_UP:
            if self.getY() >= game_area.getRect().topleft[1]+utils.PLAYER_LINE_WIDTH+utils.SHARK_INCREMENT:
                return True
        elif direction == pygame.K_DOWN:
            if self.getY() <= game_area.getRect().bottomleft[1]-utils.PLAYER_LINE_WIDTH-utils.SHARK_INCREMENT:
                return True
        elif direction == pygame.K_LEFT:
            if self.getX() >= game_area.getRect().topleft[0]+utils.PLAYER_LINE_WIDTH+utils.SHARK_INCREMENT:
                return True
        elif direction == pygame.K_RIGHT:
            if self.getX() <= game_area.getRect().topright[0]-utils.PLAYER_LINE_WIDTH-utils.SHARK_INCREMENT:
                return True
        return False

    def move(self, game_area):

        if self.getX() == self.current_poi[0] and self.getY() == self.current_poi[1]:
            self.generatePoi(game_area.getDim())
            self.current_poi = self.poi.popleft()

        valid = False

        while not valid:
            if self.getX() < self.current_poi[0]:
                direction = pygame.K_RIGHT
            elif self.getX() > self.current_poi[0]:
                direction = pygame.K_LEFT
            elif self.getY() < self.current_poi[1]:
                direction = pygame.K_DOWN
            elif self.getY() > self.current_poi[1]:
                direction = pygame.K_UP
            valid = self.validatePosition(direction,game_area)

        if direction == pygame.K_UP or direction == pygame.K_DOWN:
            self.moveY(direction, utils.SHARK_INCREMENT)
        if direction == pygame.K_LEFT or direction == pygame.K_RIGHT:
            self.moveX(direction, utils.SHARK_INCREMENT)

    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.surface

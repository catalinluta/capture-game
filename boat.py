__author__ = 'luta'
import pygame
import utils
import operator

class Boat:
    surface = None
    rect = None
    x = None
    y = None
    direction = None
    capture = False
    capturing = []
    inflection_points = []

    def __init__(self, image, x, y, direction):
        self.x = x
        self.y = y
        print(self.x,self.y)
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect()
        self.direction = direction

    def getPos(self):
        return (self.x, self.y)

    def getDrawPos(self):
        return (self.x-20, self.y-40)

    def getX(self):
        return self.x

    def moveX(self, direction, increment):
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
            if self.capture:
                self.inflection_points.append(tuple(map(operator.add, self.getPos(), self.getRect().bottomright)))
        if self.capture:
            self.capturing.append(tuple(map(operator.add, self.getPos(), self.getRect().bottomright)))

        if direction == pygame.K_RIGHT:
            self.x += increment
        if direction == pygame.K_LEFT:
            self.x -= increment

    def getY(self):
        return self.y

    def moveY(self, direction, increment):
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
            if self.capture:
                self.inflection_points.append(tuple(map(operator.add, self.getPos(), self.getRect().bottomright)))
        if self.capture:
            self.capturing.append(tuple(map(operator.add, self.getPos(), self.getRect().bottomright)))

        if direction == pygame.K_UP:
            self.y -= increment
        if direction == pygame.K_DOWN:
            self.y += increment


    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.surface

    def startCapturing(self):
        self.capture = True
        self.inflection_points.append(tuple(map(operator.add, self.getPos(), self.getRect().bottomright)))

    def move(self, direction, game_area):
        validX = False
        validY = False
        if direction == pygame.K_LEFT:
            if game_area.border_bottom.contains(self.getPos()) or game_area.border_top.contains(self.getPos()) or self.capture:
                distance = game_area.border_left.distanceX(self.getPos())
                if distance > utils.PADDING:
                    validX = True
        elif direction == pygame.K_RIGHT:
            if game_area.border_bottom.contains(self.getPos()) or game_area.border_top.contains(self.getPos()) or self.capture:
                distance = game_area.border_right.distanceX(self.getPos())
                if distance > utils.PADDING:
                    validX = True
        elif direction == pygame.K_UP:
            if game_area.border_left.contains(self.getPos()) or game_area.border_right.contains(self.getPos()) or self.capture:
                distance = game_area.border_top.distanceY(self.getPos())
                if distance > utils.PADDING:
                    validY = True
        elif direction == pygame.K_DOWN:
            if game_area.border_left.contains(self.getPos()) or game_area.border_right.contains(self.getPos()) or self.capture:
                distance = game_area.border_bottom.distanceY(self.getPos())
                if distance > utils.PADDING:
                    validY = True
        if validX:
            self.moveX(direction,min(utils.INCREMENT, distance))
        if validY:
            self.moveY(direction,min(utils.INCREMENT, distance))
        if self.capture and (self.getX() in [game_area.getRect().bottomleft[0], game_area.getRect().bottomright[0]-utils.PADDING ] or self.getY() in [game_area.getRect().topleft[1], game_area.getRect().bottomleft[1]-utils.PADDING]):
            self.capture = False
            print(self.capturing)
            print(self.inflection_points)
            self.capturing.clear()
            self.inflection_points.clear()
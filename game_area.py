__author__ = 'luta'
import pygame
import shapely
from edge import Edge

pygame.init()

class GameArea:
    width = 0
    height = 0
    surface = None
    rect = None
    player_polygon = None
    border_left = Edge(1)
    border_right = Edge(1, True)
    border_top = Edge(0, True)
    border_bottom = Edge(0)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect()
        self.border_left.addPoints([self.rect.topleft, self.rect.bottomleft])
        self.border_right.addPoints([self.rect.bottomright, self.rect.topright])
        self.border_bottom.addPoints([self.rect.bottomleft, self.rect.bottomright])
        self.border_top.addPoints([self.rect.topright, self.rect.topleft])

        print(self.border_left)
        print(self.border_bottom)
        print(self.border_right)
        print(self.border_top)

        self.generatePolygon(self.getPlayerCircuit())

    def getDim(self):
        return (self.width, self.height)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.surface

    def blit(self, surface, position):
        self.surface.blit(surface, position)

    def getPlayerCircuit(self):
        mashed = []
        mashed.extend(self.border_left.getPoints())
        mashed.extend(self.border_bottom.getPoints())
        mashed.extend(self.border_right.getPoints())
        mashed.extend(self.border_top.getPoints())
        used = []
        circuit = [x for x in mashed if x not in used and (used.append(x) or True)]
        return used

    def getPlayerPoly(self):
        return self.player_polygon

    def generatePolygon(self, list):
        self.player_polygon = shapely.Polygon(list)
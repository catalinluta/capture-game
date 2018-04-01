__author__ = 'luta'

from operator import itemgetter
import sys

def colinear(a, b, c):
   area = a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])

   return area == 0

class Edge:
    points = None
    sortBy = None
    reverse = None

    def __init__(self, sortBy, reverse=False):
        self.points = []
        self.sortBy = sortBy
        self.reverse = reverse
        pass

    def __repr__(self):
        return "Points : "+repr(self.points)+" Sort By: "+repr(self.sortBy)+ " Reverse : "+repr(self.reverse)

    def arrange(self):
        first_sort = self.sortBy
       # second_sort = abs(self.sortBy-1)

        sorted(self.points, key=itemgetter(first_sort), reverse=self.reverse)
        #sorted(self.points, key=itemgetter(second_sort), reverse=self.reverse)

    def addPoints(self, points):
        self.points.extend(points)
        self.arrange()

    def addPoint(self, point):
        self.points.append(point)
        self.arrange()

    def getPoints(self):
        return self.points

    def contains(self, point):
        for i in range(len(self.points)-1):
            if colinear(self.points[i], self.points[i+1], point):
                return True
        return False

    def distanceX(self,point):
        min = sys.maxsize
        pos = 0
        aux = 0
        aux_list = self.getPoints()
        if self.reverse:
            aux_list = list(reversed(self.getPoints()))
        for i in range(len(aux_list)-1):
            if aux_list[i][1] == aux_list[i+1][1]:
                continue
            if aux_list[i][1] <= point[1] and aux_list[i+1][1] >= point[1]:
                aux = point[0] - self.points[i][0]
                print(aux)
                if self.reverse :
                    if aux <= 0 and abs(aux) < min:
                        min = abs(aux)
                        pos = i
                else:
                    if ( aux >= 0 ) and aux < min:
                        min = aux
                        pos = i
        print(min)
        if min == sys.maxsize:
            min = -1
        return min

    def distanceY(self,point):
        min = sys.maxsize
        pos = 0
        aux = 0
        aux_list = self.getPoints()
        if self.reverse:
            aux_list = list(reversed(self.getPoints()))
        for i in range(len(aux_list)-1):
            if aux_list[i][1] != aux_list[i+1][1]:
                continue
            if aux_list[i][0] <= point[1] and aux_list[i+1][0] >= point[0]:
                aux = point[1] - self.points[i][1]
                print(aux)
                if not self.reverse :
                    if aux <= 0 and abs(aux) < min:
                        min = abs(aux)
                        pos = i
                else:
                    if ( aux >= 0 ) and aux < min:
                        min = aux
                        pos = i
        print(min)
        if min == sys.maxsize:
            min = -1
        return min


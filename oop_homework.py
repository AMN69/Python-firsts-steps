import math

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        distance = math.sqrt(((self.coor2[0] - self.coor1[0]) ** 2) + ((self.coor2[1] - self.coor1[1]) ** 2)) 
        print("Distance between ({}, {}) and ({}, {}) is: {}".format(self.coor1[0], self.coor1[1], self.coor2[0], self.coor2[1], distance))
    def slope(self):
        slope = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        print("Slope between ({}, {}) and ({}, {}) is {}".format(self.coor1[0], self.coor1[1], self.coor2[0], self.coor2[1], slope))

coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
li.distance()
li.slope()

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        volume = math.pi * self.radius ** 2 * self.height
        print("Volume for a cylinder with height {} and radius {} is: {}".format(self.height, self.radius, volume))
    def surface_area(self):
        surface = (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius ** 2)
        print("Surface area for a cylinder with height {} and radius {} is: {}".format(self.height, self.radius, surface))

c = Cylinder(2,3)
c.volume()
c.surface_area()
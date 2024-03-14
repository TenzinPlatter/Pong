import random
import pygame
import Globals as G

class Ball():

    def __init__(self):
        self.coordinate = [random.randrange(600, 800), random.randrange(400, 500)]
        self.velocity = [10, 10]
        self.radius = 50
        self.nextCollision = [0, 0]
        self.recentlyCollided = True


    def Draw(self, window):
        pygame.draw.circle(window, G.WHITE, self.coordinate, self.radius)
    
    def Move(self, calculating = False):
        tempX, tempY = G.addLists(self.coordinate, self.velocity)
        if tempX > 1870 or tempX < 50:
            self.velocity[G.X] *= -1
        if tempY > 1030 or tempY < 50:
            self.velocity[G.Y] *= -1
        self.coordinate = G.addLists(self.coordinate, self.velocity)

    def FindNextCollision(self):
        pass
    
    def Update(self):
        self.Move()
        if self.recentlyCollided:
            self.nextCollision = self.FindNextCollision()
            self.recentlyCollided = False

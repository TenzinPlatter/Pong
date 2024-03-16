import random
import pygame
import Globals as G

'''
started function to find next collision, part of ball class

    def NextCollision(self):
        #finds coordinate of balls next collision
        nextCollisionCoordinate = [0, 0]
        currCoord = [self.x, self.y]
        hasHit = False
        while not hasHit:
            currCoord = self.Move(True, currCoord)
            collision = self.Collision()
            hasHit = collision()[G.HITPADDLE] or collision[G.HITBORDER]
'''          


class Ball():

    def __init__(self):
        self.coordinate = [random.randrange(600, 800), random.randrange(400, 500)]
        self.velocity = [10, 10]
        self.radius = 50
        self.nextCollision = [0, 0]
        self.recentlyCollided = True


    def Draw(self, window):
        pygame.draw.circle(window, G.WHITE, self.coordinate, self.radius)
    
    def Move(self, calculating = False, tempCoord = [0, 0]):
        tempX, tempY = G.addLists(self.coordinate, self.velocity)
        if tempX > 1870 or tempX < 50:
            self.velocity[G.X] *= -1
        if tempY > 1030 or tempY < 50:
            self.velocity[G.Y] *= -1
        if calculating:
            return G.addLists(tempCoord, self.velocity)
        else:
            self.coordinate = G.addLists(self.coordinate, self.velocity)
    
    def Update(self, paddles):
        self.Move()
        for paddle in paddles:
            self.Collision(paddle)
        if self.recentlyCollided:
            #self.nextCollision = self.NextCollision()
            self.recentlyCollided = False

    def Collision(self, paddle, x = -1, y = -1):
        #returns tuple of booleans - (hitPaddle, hitBorder) - if x and y not passed in
        #uses balls coordinates
            if x == -1 or y == -1:
                x = self.coordinate[G.X]
                y = self.coordinate[G.Y]
            hitPaddle = False
            hitBorder = False
            if x < 150 or x > 1770:
                if y < paddle.rect.top + 125 and y > paddle.rect.top - 125:
                    hitPaddle = True
                else:
                    hitBorder = True



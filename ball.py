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
        self.coordinate = [random.randrange(G.WINSIZE[G.X]/2 - 100, G.WINSIZE[G.X]/2 + 100), random.randrange(G.WINSIZE[G.Y]/2 - 100, G.WINSIZE[G.Y]/2 + 100)]
        self.velocity = [12, 12]
        self.radius = 15

    def Draw(self, window):
        pygame.draw.circle(window, G.WHITE, self.coordinate, self.radius)
    
    def Move(self):
        tempX, tempY = G.addLists(self.coordinate, self.velocity)

        if tempX < 90 or tempX > 1310: return "reset"


        if tempX > G.WINSIZE[G.X] - self.radius or tempX < self.radius:
            self.velocity[G.X] *= -1
        if tempY > G.WINSIZE[G.Y] - self.radius or tempY < self.radius:
            self.velocity[G.Y] *= -1

        self.coordinate = G.addLists(self.coordinate, self.velocity)
    
    def Update(self, playerPaddle, computerPaddle):
        if self.velocity[G.X] > 0:
            computerCollision = self.Collision(computerPaddle)
            if computerCollision: self.velocity[G.X] *= -1
        else:
            playerCollision = self.Collision(playerPaddle)
            if playerCollision: self.velocity[G.X] *= -1

        if self.Move() == "reset": self.Reset()


    def Collision(self, paddle):
        x = self.coordinate[G.X]
        y = self.coordinate[G.Y]
        hitPaddle = False
        if x < 115 or x > G.WINSIZE[G.X] - 115:
            if y + 30 > paddle.rect.top and y < paddle.rect.top + 230: #added some extra space above paddle where ball will still collide so it feels more forgiving
                G.collisionSound.play()
                hitPaddle = True
        return hitPaddle



    def Reset(self):
        G.resetSound.play()
        self.coordinate = [random.randrange(G.WINSIZE[G.X]/2 - 100, G.WINSIZE[G.X]/2 + 100), random.randrange(G.WINSIZE[G.Y]/2 - 100, G.WINSIZE[G.Y]/2 + 100)]
        self.velocity = [12,12]
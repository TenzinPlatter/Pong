import pygame
import Globals as G

class Paddle():

    def __init__(self, x, y, isPlayer) -> None:
        self.size = 200
        self.rect = pygame.Rect(x, y, 30, self.size)
        self.colour = G.WHITE
        self.isPlayer = isPlayer

    def Draw(self, window):
        #draws paddle rect onto window passed into function
        pygame.draw.rect(window, self.colour, self.rect)

    def Move(self, ball):
        y = 0
        #add option to move with either mouse or keyboard
        if self.isPlayer:
            #if is player paddle moves with arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y = -10
            if keys[pygame.K_DOWN]:
                y = 10
        
        else:
            #follows y coordinate of ball with a max speed
            distance = ball.coordinate[G.Y] - self.rect.top - 100
            if  abs(distance) > G.PADDLESPEED: 
                if distance < 0:
                    y = G.PADDLESPEED * -1
                else:
                    y = G.PADDLESPEED 
            else:
                y = distance
        if self.rect.top + y < 0: y = -1 * self.rect.top
        #smthing here deletes the paddle when it hits the bottom of the screen
        elif  self.rect.top + y > G.WINSIZE[G.Y] - self.size: y = G.WINSIZE[G.Y] - self.rect.top - self.size

        self.rect = self.rect.move(0, y)



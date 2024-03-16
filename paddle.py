import pygame
import Globals as G

class Paddle():

    def __init__(self, x, y, isPlayer) -> None:
        self.rect = pygame.Rect(x, y, 30, 250)
        self.colour = G.WHITE
        self.isPlayer = isPlayer

    def Draw(self, window):
        #draws paddle rect onto window passed into function
        pygame.draw.rect(window, self.colour, self.rect)

    def Move(self, ball):
        if self.isPlayer:
            #if is player paddle moves with arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect = self.rect.move(0, -10)
            if keys[pygame.K_DOWN]:
                self.rect = self.rect.move(0, 10)
        
        else:
            #follows y coordinate of ball with a max speed
            distance = ball.coordinate[G.Y] - self.rect.top - 125
            if  abs(distance) > G.paddleSpeed:
                self.rect = self.rect.move(0, G.paddleSpeed * (-1 * (distance < 0)))  
            else:
                self.rect = self.rect.move(0, distance)



import pygame
import Globals as G

class Paddle():

    def __init__(self, x, y, isPlayer) -> None:
        self.rect = pygame.Rect(x, y, 30, 250)
        self.colour = G.WHITE
        self.isPlayer = isPlayer

    def Draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

    def Move(self):
        if self.isPlayer:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect = self.rect.move(0, -10)
            if keys[pygame.K_DOWN]:
                self.rect = self.rect.move(0, 10)
        
        else:
            pass


    def BallCollision(self):
        
        

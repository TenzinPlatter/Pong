import pygame
from pygame import *
import Globals as G
import ball as Ball
import paddle as Paddle

class App():
    def __init__(self):
        pygame.init()
        self.inGame = True
        self.window = pygame.display.set_mode(G.WINSIZE)
        pygame.display.set_caption("Pong")
        self.ball = Ball.Ball()
        self.clock = pygame.time.Clock()
        self.playerPaddle = Paddle.Paddle(100, 415, True)
        self.computerPaddle = Paddle.Paddle(1820, 415, False)

        while self.inGame:
            self.clock.tick(G.FPS)
            self.Update()
            self.OnEvent()
            self.Render()
        
        self.Quit()

    def Render(self):
        self.window.fill(G.BLACK)
        self.ball.Draw(self.window)
        self.playerPaddle.Draw(self.window)
        self.computerPaddle.Draw(self.window)

        pygame.display.update()

    def Update(self):
        self.ball.Update()
        self.playerPaddle.Move()
        self.computerPaddle.Move()

    def OnEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
    
    def Quit(self):
        pygame.quit()


App()
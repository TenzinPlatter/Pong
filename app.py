import pygame
from pygame import *
import Globals as G
import ball as Ball
import paddle as Paddle

class App():
    def __init__(self):
        #initializes all values
        pygame.init()
        self.inGame = True
        self.window = pygame.display.set_mode(G.WINSIZE)
        pygame.display.set_caption("Pong")
        self.ball = Ball.Ball()
        self.clock = pygame.time.Clock()
        self.playerPaddle = Paddle.Paddle(100, 415, True)
        self.computerPaddle = Paddle.Paddle(1820, 415, False)

        while self.inGame:
            #game loop for when playing, need some larger loop to handle points 
            self.clock.tick(G.FPS)
            self.Update()
            self.OnEvent()
            self.Render()
        
        self.Quit()

    def Render(self):
        #fill screen black to overwrite last frame then draws paddles and ball
        self.window.fill(G.BLACK)
        self.ball.Draw(self.window)
        self.playerPaddle.Draw(self.window)
        self.computerPaddle.Draw(self.window)

        pygame.display.update()

    def Update(self):
        #updates ball - (moves and need to add calculation for next collision) - and moves paddles
        self.ball.Update((self.playerPaddle, self.computerPaddle))
        self.playerPaddle.Move(self.ball)
        self.computerPaddle.Move(self.ball)

    def OnEvent(self):
        #checks for quit
        for event in pygame.event.get():
            if event.type == QUIT:
                self.inGame = False
    
    def Quit(self):
        #closes pygame
        pygame.quit()


App()
import pygame
from pygame import *
import Globals as G 
import ball as Ball
import paddle as Paddle

class App():
    def __init__(self):
        #initializes all values
        pygame.init()
        pygame.mixer.init()
        self.inGame = False
        self.inMenu = True
        self.window = pygame.display.set_mode(G.WINSIZE)
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(.1)

        while self.inMenu:
            self.clock.tick(G.FPS)
            self.OnEvent()
            self.Render()

        self.ball = Ball.Ball()
        self.playerPaddle = Paddle.Paddle(100, G.WINSIZE[G.Y]/2 + 100, True)
        self.computerPaddle = Paddle.Paddle(G.WINSIZE[G.X] - 100, G.WINSIZE[G.Y]/2 + 100, False)
        while self.inGame:
            #game loop for when playing, need some larger loop to handle points 
            self.clock.tick(G.FPS)
            self.OnEvent()
            self.Update()
            self.Render(inGame = True)
        
        self.Quit()


    def menuScreen(self):
        #draws menu
        G.drawText("Pong", G.WHITE, G.WINSIZE[G.X]/2, 250, self.window)
        G.drawText("Press Space to Start", G.WHITE, G.WINSIZE[G.X]/2, 550, self.window)
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            self.inGame = True
            self.inMenu = False
 


    def Render(self, inGame = False):
        #fill screen black to overwrite last frame then draws paddles and ball
        self.window.fill(G.BLACK)
        if inGame:
            self.ball.Draw(self.window)
            self.playerPaddle.Draw(self.window)
            self.computerPaddle.Draw(self.window)
        else:
            self.menuScreen()

        pygame.display.update()

    def Update(self):
        #updates/moves ball and moves paddles
        self.ball.Update(self.playerPaddle, self.computerPaddle)
        self.playerPaddle.Move(self.ball)
        self.computerPaddle.Move(self.ball)


    def OnEvent(self):
        #checks for quit
        for event in pygame.event.get():
            if event.type == QUIT:
                self.inGame = False
                self.inMenu = False
    
    def Quit(self):
        #closes pygame
        pygame.quit()


App()
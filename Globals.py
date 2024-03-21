from cgitb import reset
from operator import add
import pygame

WINSIZE = 1400, 900
X = 0
Y = 1
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HITPADDLE = 0
HITBORDER = 1
PADDLESPEED = 10
ballVeloIncrement = [.2, .2]


def addLists(list1, list2):
    return list(map(add, list1, list2))


pygame.mixer.init()
music = pygame.mixer.music.load("music.mp3")
collisionSound = pygame.mixer.Sound("hitEffect.mp3")
collisionSound.set_volume(.1)
resetSound = pygame.mixer.Sound("resetSound.mp3")
resetSound.set_volume(.15)
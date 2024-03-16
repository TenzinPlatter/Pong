from operator import add

WINSIZE = 1920, 1080
X = 0
Y = 1
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HITPADDLE = 0
HITBORDER = 1
PADDLESPEED = 10
BALLVECLOCITYINCREMENT= [5, 5]


def addLists(list1, list2):
    return list(map(add, list1, list2))
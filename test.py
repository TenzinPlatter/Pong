'''
import pygame
from pygame import *

pygame.init()
hi = pygame.Rect(50,400,50,50)


running = True
window = pygame.display.set_mode((500, 500))
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    flag = True
    if hi.top > -100 and flag:
        hi = hi.move(0, -1)
    else:
        hi = hi.move(0, 1)
        flag = False
    window.fill(0)
    pygame.draw.rect(window, 255, hi)
    pygame.display.update()

pygame.quit()
'''



list1 = [1,2]

list2 = list(map(lambda val: val * -1, list1))
print(list2)
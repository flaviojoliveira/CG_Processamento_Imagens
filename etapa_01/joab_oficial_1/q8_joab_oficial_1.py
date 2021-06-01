import time

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('Hello Joab')

screen.fill(BLACK)

pygame.draw.line(screen, WHITE, [10, 100], [630, 100], 5)
pygame.draw.rect(screen, BLUE, [200, 210, 40, 20])
pygame.draw.ellipse(screen, RED, [300, 200, 40, 40])
pygame.draw.polygon(screen, GREEN, [[420, 200], [440, 240], [400, 240]])

pygame.display.flip()

time.sleep(5)

screen.fill(BLACK)

text = font.render('pygame', True, WHITE)
screen.blit(text, [250, 200])

pygame.display.flip()

time.sleep(5)


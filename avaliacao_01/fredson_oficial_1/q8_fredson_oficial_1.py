import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for i in range(1, 5):
        pygame.draw.rect(screen, (1*i, 45*i, 30*i), pygame.Rect(30*i, 30*i, 60*i, 60*i))
        pygame.display.flip()
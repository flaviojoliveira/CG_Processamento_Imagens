import pygame

#===tamanho=========
WITH= 900
HEIGHT= 600

#==cores=========
PURPLE= (148,0,211)
BLUE= (0,0,255)
GREEN =(34,139,34)
BLACK=(0,0,0)
RED=(255,0,0)
WHITE = (255,255,255)

backG = pygame.display.set_mode((WITH, HEIGHT))

def tela():
    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
        backG.fill(WHITE)
        pygame.draw.rect(backG, RED, (300, 300, 300, 400))
        pygame.draw.circle(backG, BLUE, [600,250], 40)
        pygame.draw.line(backG, GREEN,  [320, 240], [290, 240], 5) 
        pygame.draw.ellipse(backG, PURPLE, [300, 10, 50, 20])
        pygame.draw.polygon(backG, BLACK, [[100, 100], [450, 0], [600, 200]], 2)
      
      



        pygame.display.update()

    pygame.quit()
    quit ()

if __name__ == "__main__":
    tela()


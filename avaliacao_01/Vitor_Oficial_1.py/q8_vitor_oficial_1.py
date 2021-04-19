import pygame

#===tamanho=========
WITH= 800
HEIGHT= 500

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
        pygame.draw.rect(backG, RED, (110, 330, 30, 250))
        pygame.draw.polygon(backG, BLACK, [[600, 60], [70, 0], [80, 100]], 2)
        pygame.draw.circle(backG, BLUE, [600,250], 40)
        pygame.draw.line(backG, GREEN,  [320, 240], [230, 250], 5) 
        pygame.draw.ellipse(backG, PURPLE, [200, 60, 70, 20]) 
      
        pygame.display.update()

    pygame.quit()
    quit ()

if __name__ == "__main__":
    tela()

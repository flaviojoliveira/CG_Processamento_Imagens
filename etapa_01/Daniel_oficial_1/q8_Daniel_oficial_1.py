import pygame

#Pygame init
pygame.init()

largura= 640
altura=480

#Cores DISPLAY
roxo_escuro= (148,0,211)
azul= (0,0,255)
verde =(34,139,34)
preto=(0,0,0)
branco=(255,255,255)
vermelho=(255,0,0)

#Tamanho da janela
fundo = pygame.display.set_mode((largura,altura))

#Define um título na janela.
pygame.display.set_caption("Desenhos")



def formas():
    sair = True
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
        fundo.fill(roxo_escuro)
        pygame.draw.rect(fundo, vermelho, (150, 10, 20, 50))
        pygame.draw.circle(fundo, azul, [60,250], 40)
        pygame.draw.line(fundo, verde,  [320, 240], [290, 240], 5) 
        pygame.draw.ellipse(fundo, vermelho, [300, 10, 50, 20])
        pygame.draw.polygon(fundo, preto, [[100, 100], [0, 200], [200, 200]], 2)
        pygame.draw.lines(fundo, preto, [0, 80], [[50, 90], [200, 80], [220, 30]], 5)
      



        pygame.display.update()

    pygame.quit()
    quit ()

def main():
    formas()

main()

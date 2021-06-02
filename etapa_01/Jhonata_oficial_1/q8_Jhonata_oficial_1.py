import pygame
import math
amigo = []


# menuLetras
q = 0
q == int(1)

# cores
rosa = (255, 228, 196)
azul = (0, 0, 255)
verde = (34, 139, 34)
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
ouro = (218, 165, 32)
magenta = (255, 0, 255)
PI = math.pi
pygame.init()

largura = 640
altura = 480
pos_x = int(largura/2)
pos_y = int(altura/2)

# Seta o tamanho da janela
fundo = pygame.display.set_mode((largura, altura))
# define um título na janela.
pygame.display.set_caption("Desenhos geometricos")


def menu():


    while True:
        print('''Menu:
        Tecla ‘q’ para desenhar o primeiro retângulo.
        Tecla ‘w’ para desenhar o segundo retângulo.
        Tecla ‘e’ para desenhar a primeira elipse.
        Tecla ‘r’ para desenhar a segunda elipse.
        Tecla ‘t’ para desenhar o polígono.
        Tecla ‘y’ para desenhar o círculo.
        Tecla ‘u’ para desenhar o arco.
        Tecla 'x' para sair.''')
        op = input("Opção selecionada: ")

        if(op == 'q'):
            primerioRetangulo()
        elif(op == 'w'):
            segundoRetangulo()
        elif(op == 'e'):
            primeiraElipse()
        elif(op == 'r'):
            segundoElipse()
        elif(op == 't'):
            poligono()
        elif(op == 'y'):
            circulo()
        elif(op == 'u'):
            arco()
        

        else:
            break


def primerioRetangulo():
    fundo.fill(rosa)
    pygame.draw.rect(fundo, vermelho, (150, 10, 20, 50))
    pygame.display.update()


def segundoRetangulo():
    fundo.fill(rosa)
    pygame.draw.rect(fundo, ouro, (150, 10, 20, 50))
    pygame.display.update()


def primeiraElipse():
    fundo.fill(rosa)
    pygame.draw.ellipse(fundo, vermelho, [300, 10, 50, 20])
    pygame.display.update()


def segundoElipse():
    fundo.fill(rosa)
    pygame.draw.ellipse(fundo, magenta, [300, 10, 50, 20])
    pygame.display.update()

def poligono():
    fundo.fill(rosa)
    pygame.draw.polygon(fundo, preto, [[100, 100], [0, 200], [200, 200]], 2)
    pygame.display.update()


def arco():
    fundo.fill(rosa)
    pygame.draw.arc(fundo, vermelho, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
    pygame.display.update()


def circulo():
    fundo.fill(rosa)
    pygame.draw.circle(fundo, azul, [60, 250], 40)
    pygame.display.update()


def main():
    menu()


main()

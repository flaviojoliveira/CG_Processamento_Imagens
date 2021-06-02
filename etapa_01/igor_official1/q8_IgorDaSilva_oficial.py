import pygame
import math
amigo = []


# menuLetras
q = 0
q == int(1)

# cores
pink = (255, 228, 196)
blue = (0, 0, 255)
green = (34, 139, 34)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gold = (218, 165, 32)
magenta = (255, 0, 255)
PI = math.pi
pygame.init()

width = 640
height = 480
pos_x = int(width/2)
pos_y = int(height/2)

# Seta o tamanho da janela
backgraund = pygame.display.set_mode((width, height))
# define um título na janela.
pygame.display.set_caption("Results")


def menu():


    while True:
        print('''Menu:
        Press "q" to print first rectangle.
        Press "w" to print second rectangle.
        Press "e" to print first ellipse.
        Press "r" to print second elipse.
        Press "t" to print polygon.
        Press "y" to print circle.
        Press "u" to print bow.
        Press "x" to Exit.''')
        op = input(" Option selected: ")

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
    backgraund.fill(pink)
    pygame.draw.rect(backgraund, red, (150, 10, 20, 50))
    pygame.display.update()


def segundoRetangulo():
    backgraund.fill(pink)
    pygame.draw.rect(backgraund, ouro, (150, 10, 20, 50))
    pygame.display.update()


def primeiraElipse():
    backgraund.fill(pink)
    pygame.draw.ellipse(backgraund, red, [300, 10, 50, 20])
    pygame.display.update()


def segundoElipse():
    backgraund.fill(pink)
    pygame.draw.ellipse(backgraund, magenta, [300, 10, 50, 20])
    pygame.display.update()

def poligono():
    backgraund.fill(pink)
    pygame.draw.polygon(backgraund, black, [[100, 100], [0, 200], [200, 200]], 2)
    pygame.display.update()


def arco():
    backgraund.fill(pink)
    pygame.draw.arc(backgraund, red, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
    pygame.display.update()


def circulo():
    backgraund.fill(pink)
    pygame.draw.circle(backgraund, azul, [60, 250], 40)
    pygame.display.update()


def main():
    menu()


main()

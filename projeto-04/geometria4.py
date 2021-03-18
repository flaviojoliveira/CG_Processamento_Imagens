from PIL import Image
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

# unidade 2 - Geometria | Sintetizando Imagens - Bandeiras
def bandeira_franca(height):
    WHITE = (255, 255, 255)
    BLUE = (0, 85, 164)
    RED = (239, 65, 53)
    width = 3*height//2
    offset = width//3

    image = Image.new("RGB", (width, height), WHITE)
    for x in range(offset):
        for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2*offset, y), RED)

    return image

if __name__ == "__main__":
 #   t = triangulo(700)
 #    t.show()
 bandeira = bandeira_franca(450)
 bandeira.show()
    
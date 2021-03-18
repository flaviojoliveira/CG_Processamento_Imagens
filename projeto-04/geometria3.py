from PIL import Image
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

# unidade 2 - Geometria | Sintetizando Imagens
def in_path(filename):
    return os.path.join(INPUT_DIR, filename)

def triangulo(size):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    image = Image.new("RGB", (size, size), WHITE)
    for x in range(size):
        for y in range(size):
            if x < y:
                image.putpixel((x,y), BLACK)
    
    return image

if __name__ == "__main__":
    t = triangulo(700)
    t.show()
    
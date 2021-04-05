from PIL import Image

# from utils import in_file
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def bandeira_japao(height):
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)
    width = 3*height//2
    r = 3*height//10
    c = (width//2, height//2)

    image = Image.new("RGB", (width, height), WHITE)
    for x in range(c[0]-r, c[0]+ r):
        for y in range(c[1]-r, c[1]+ r):
            if (x-c[0])**2 + (y-c[1])**2 <= r**2:
                image.putpixel((x, y), RED)

    return image

if __name__ == "__main__":
    t = bandeira_japao(700)
    t.show()
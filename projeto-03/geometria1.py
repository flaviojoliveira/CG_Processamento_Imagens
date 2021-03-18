from PIL import Image
import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"

# unidade 2 - Geometria | Sintetizando Imagens
def in_path(filename):
    return os.path.join(INPUT_DIR, filename)
image = Image.new("RGB", (600, 600))

image.show()
from PIL import Image
from utils import infile
import os

#abre imagem
image = Image.open(infile("bandeira.jpeg"))

#exiba na tela o valor do pixel na posição determinado
print(image.getpixel((112,55)))

#retorno
image.show()
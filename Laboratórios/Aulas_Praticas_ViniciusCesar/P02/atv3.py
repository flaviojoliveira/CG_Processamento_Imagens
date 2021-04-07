import Image
from PIL import Image

im=image.open('imagem.png')

print(im.size)

im= im.rotate(45, expand=1)

print(im.size)

im.save("rotacao2.png")
im.show
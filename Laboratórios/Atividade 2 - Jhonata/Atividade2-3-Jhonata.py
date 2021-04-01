#import Image
from PIL import Image

imagem = Image.open("line.png")

print(imagem.size)

imagem = imagem.rotate(270)

print(imagem.size)

imagem.save("rotacao2.png")
imagem.show()

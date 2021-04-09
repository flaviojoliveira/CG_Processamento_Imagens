from PIL import Image

im = Image.open("imagem.png")

print(im.size)

im = im.rotate(270, expand=1)

print(im.size)

im.save("rotacao2.png")
im.show()

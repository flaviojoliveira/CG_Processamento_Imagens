from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

imagem = Image.open("../../data/input/q9_fig.jpg")
print(imagem.format)
print(imagem.mode)

data = image.imread("../../data/input/q9_fig.jpg")
print(data.dtype)
print(data.shape)
print(data.max())
print(data.min())

pyplot.imshow(data)


imagem2 = Image.fromarray(data)
print(type(imagem2))

data2 = asarray(imagem)
print(data2.dtype)
print(data2.shape)

imagem2.save("../../data/input/q9_fig.png",format="PNG")
imagem2.save("../../data/input/q9_fig.gif",format="GIF")

imagem3 = Image.open("../../data/input/q9_fig.gif")
print(imagem3.format)

imagem_cinza = imagem.convert(mode="L")
imagem_cinza.save("../../data/input/q9_fig_cinz.png",format="PNG")

print(imagem_cinza.size)
imagem_cinza.thumbnail((80,80))

print(imagem_cinza.thumbnail((80,80)))
horizontal_image = imagem.transpose(Image.FLIP_LEFT_RIGHT)

horizontal_image.save("../../data/input/q9_fig_invert.png",format="PNG")
pyplot.imshow(imagem.crop((70,70,100,100)))
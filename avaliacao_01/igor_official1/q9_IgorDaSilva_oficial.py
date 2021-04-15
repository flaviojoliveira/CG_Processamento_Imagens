from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

local = "../../data/input/q9_fig.jpg"
#Armazendando a imagem em uma variável
imagem = Image.open(local)

#Formato
print(imagem.format)

#Modo do Canal
print(imagem.mode)

#Propriedades da imagem como array
data = image.imread(local)
print(data.dtype)
print(data.shape)
print(data.max())
print(data.min())

#Array de Pixel como Imagem
pyplot.imshow(data)

#Convertendo para Pillow
imagem2 = Image.fromarray(data)
#Verificando o Tipo
print(type(imagem2))

#Convertendo para um array numpy
data2 = asarray(imagem)

#Imprimindo os Atributos
print(data2.dtype)
print(data2.shape)

#Salvar Imagem como PNG
imagem2.save("../../data/input/q9_fig.png",format="PNG")
#Salvar Imagem com GIF
imagem2.save("../../data/input/q9_fig.gif",format="GIF")

#Exibir a imagem e verificar o formato
imagem3 = Image.open("../../data/input/q9_fig.gif")
print(imagem3.format)

#Escala grey
imagem_grey = imagem.convert(mode="L")
imagem_grey.save("../../data/input/q9_fig_cinz.png",format="PNG")

#Exibir Tamanho 

print(imagem_grey.size)

#Gerando Thumbnail ignorando Aspecto Ratio
imagem_grey.thumbnail((80,80))

print(imagem_grey.thumbnail((80,80)))

#Inveter a Imagem
horizontal_image = imagem.transpose(Image.FLIP_LEFT_RIGHT)

horizontal_image.save("../../data/input/q9_fig_invert.png",format="PNG")

#Exibir Coordenadas Especificas

pyplot.imshow(imagem.crop((70,70,100,100))) 
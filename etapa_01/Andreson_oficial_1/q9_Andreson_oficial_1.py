from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

image = Image.open("./avaliacao_01/Andreson_oficial_1/q6.jpg")

# Exibir o formato do arquivo;
print(image.format)
  # Exibir o modo do canal formato de pixel
print(image.mode)
  # Dimensão da imagem em pixel
print(image.size)
  # Exibir as propriedades da imagem em um array de pixel

data = image.imread("./avaliacao_01/Andreson_oficial_1/q6.jpg")

image2 = Image.fromarray(data)
  # Exibir o array de pixel como imagem
image2 = Image.fromarray(data)
  # converter o array de pixel em objeto Image Pillow
pil_image=Image.fromarray(np_array)
  # verificar o tipo do objeto
type(image2)
  # converter um objeto do tipo imagem para um array numpy
im = PIL.Image.fromarray(numpy.uint8(I))
  # Imprimir em tela os atributos do array
print(data.dtype)
print(data.shape)
  # imprimir (salvar) a imagem no formato PNG
image.save("sample_data/imagens/brasilia.png",format="PNG")
  # imprimir (salvar) a imagem no formato GIF
image.save("sample_data/imagens/brasilia.gif",format="GIF")
  # Exibir a imagem e verificar o formato:
print(image3.format)
  # Converter a imagem em escala de cinza
image_gray = image.convert(mode="L")
image_gray
  # Exibir tamanho
print(image.size)
  # Gerar thumbnail ignorando aspecto ratio
image_gray.thumbnail((100,100))
  # Flip da imagem (inverter)
horizontal_image = image2.transpose(Image.FLIP_LEFT_RIGHT)
  # Exibir coordenadas específicas
pyplot.imshow(horizontal_image)